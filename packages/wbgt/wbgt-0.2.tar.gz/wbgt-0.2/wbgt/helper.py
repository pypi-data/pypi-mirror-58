import numpy as np

M_AIR: float = 28.97
CZA_MIN: float = 0.00873
NORMSOLAR_MAX: float = 0.85
REF_HEIGHT: float = 2.0
MIN_SPEED: float = 0.13
CONVERGENCE: float = 0.02
MAX_ITER: int = 50


# define physical constants
SOLAR_CONST = 1367.
GRAVITY = 9.807
STEFANB = 5.6696E-8
Cp =1003.5
M_AIR = 28.97
M_H2O = 18.015
RATIO =( Cp*M_AIR/M_H2O )
R_GAS =8314.34
R_AIR= ( R_GAS/M_AIR )
Pr= ( Cp / ( Cp + 1.25*R_AIR ) )

# define wick constants
EMIS_WICK = 0.95
ALB_WICK = 0.4
D_WICK = 0.007
L_WICK = 0.0254

#
# /* ============================================================================
#  *  Purpose: calculate the viscosity of air, kg/(m s)
#  *
#  *  Reference: BSL, page 23.
#  */
def viscosity(Tair: int):
    # Tair  /* air temperature, K */

    sigma: float = 3.617
    eps_kappa: float = 97.0
    Tr: float = Tair / eps_kappa;

    omega: float = ( Tr - 2.9 ) / 0.4 * ( -0.034 ) + 1.048;
    return( 2.6693E-6 * np.sqrt( M_AIR*Tair ) / ( sigma * sigma * omega ) );


# /* ============================================================================
#  *  Purpose: estimate the stability class
#  *
#  *  Reference: EPA-454/5-99-005, 2000, section 6.2.5
#  */
def stab_srdt(is_daytime: bool, speed: float, solar: float, dT: float) -> int:
    lsrdt = np.array([
        [ 1, 1, 2, 4, 0, 5, 6, 0 ],
        [ 1, 2, 3, 4, 0, 5, 6, 0 ],
        [ 2, 2, 3, 4, 0, 4, 4, 0 ],
        [ 3, 3, 4, 4, 0, 0, 0, 0 ],
        [ 3, 4, 4, 4, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    ])

    if is_daytime:
            if solar >= 925.0:
                j = 0
            elif  solar >= 675.0:
                j = 1
            elif solar >= 175.0:
                j = 2
            else:
                j = 3

            if speed >= 6.0:
                i = 4
            elif speed >= 5.0:
                i = 3
            elif speed >= 3.0:
                i = 2
            elif speed >= 2.0:
                i = 1;
            else:
                i = 0;
    else:
            if dT >= 0.0:
                j = 6
            else:
                j = 5

            if speed >= 2.5:
                i = 2
            elif speed >= 2.0:
                i = 1
            else:
                i = 0

    return lsrdt[i][j]


# /* ============================================================================
#  *  Purpose: estimate 2-m wind speed for all stability conditions
#  *
#  *  Reference: EPA-454/5-99-005, 2000, section 6.2.5
#  */
def est_wind_speed(speed: float, zspeed: float, stability_class: int, urban: bool) -> int:

    urban_exp = np.array([ 0.15, 0.15, 0.20, 0.25, 0.30, 0.30 ])
    rural_exp = np.array([ 0.07, 0.07, 0.10, 0.15, 0.35, 0.55 ])

    if urban:
        exponent = urban_exp[stability_class-1];
    else:
        exponent = rural_exp[stability_class-1];

    est_speed = speed * np.power( REF_HEIGHT/zspeed, exponent );
    est_speed = np.max([ est_speed, MIN_SPEED ]);
    return est_speed;


# /* ============================================================================
#  *  Purpose: calculate the saturation vapor pressure (mb) over liquid water
#  *           (phase = 0) or ice (phase = 1).
#  *
#  *  Reference: Buck's (1981) approximation (eqn 3) of Wexler's (1976) formulae.
#  */
def esat(tk: float, phase: int) -> float:
    is_liquid = phase == 0
    is_ice = phase == 1

    if is_liquid:
        y = (tk - 273.15)/(tk - 32.18)
        es = 6.1121 * np.exp(17.502 * y);
    elif is_ice:
        y = (tk - 273.15)/(tk - 0.6)
        es = 6.1115 * np.exp(22.452 * y)
    else:
        raise 'Unexpected phase'

    es = 1.004 * es;
    return es ;


# /* ============================================================================
#  *  Purpose: calculate the dew point (phase=0) or frost point (phase=1)
#  *           temperature, K.
#  */
#
# * e: (vapor) pressure mb
def dew_point(e: float, phase: int) -> float:
    is_liquid = phase == 0
    is_ice = phase == 1

    if is_liquid:
        # dew point
        z = np.log(e / (6.1121*1.004));
        tdk = 273.15 + 240.97*z/(17.502-z);
    elif is_ice:
        # frost point
        z = np.log(e / (6.1115*1.004));
        tdk = 273.15 + 272.55*z/(22.452-z);
    else:
        raise 'Unexpected phase'

    return tdk;

# /* ============================================================================
#  *  Purpose: calculate the diffusivity of water vapor in air, m2/s
#  *
#  *  Reference: BSL, page 505.
#  */
#
# floatTair,/* Air temperature, K */
# Pair; /* Barometric pressure, mb */
def diffusivity(t_air: float, p_air: float) -> float:
    Pcrit_air = 36.4
    Pcrit_h2o = 218.
    Tcrit_air = 132.
    Tcrit_h2o = 647.3
    a = 3.640E-4
    b = 2.334

    Pcrit13  = np.power( ( Pcrit_air * Pcrit_h2o ),(1./3.) );
    Tcrit512 = np.power( ( Tcrit_air * Tcrit_h2o ),(5./12.) );
    Tcrit12  = np.sqrt( Tcrit_air * Tcrit_h2o );
    Mmix = np.sqrt( 1./M_AIR + 1./M_H2O );
    Patm = p_air / 1013.25 # convert pressure from mb to atmospheres

    return( a * np.power( (t_air/Tcrit12),b) * Pcrit13 * Tcrit512 * Mmix / Patm * 1E-4 );


# /* ============================================================================
#  *  Purpose: calculate the heat of evaporation, J/(kg K), for temperature
#  *           in the range 283-313 K.
#  *
#  *  Reference: Van Wylen and Sonntag, Table A.1.1
#  */
#  floatTair;/* air temperature, K */
#  no test
def evap(t_air: float) -> float:
    return( (313.15 - t_air)/30. * (-71100.) + 2.4073E6 );


# /* ============================================================================
#  *  Purpose: calculate the thermal conductivity of air, W/(m K)
#  *
#  *  Reference: BSL, page 257.
#  */
#  float	Tair;	/* air temperature, K */
def thermal_cond(t_air: float) -> float:
    return(( Cp + 1.25 * R_AIR ) * viscosity(t_air));


# /* ============================================================================
#  * Purpose: to calculate the convective heat transfer coefficient in W/(m2 K)
#  *          for a long cylinder in cross flow.
#  *
#  * Reference: Bedingfield and Drew, eqn 32
#  *
#  */
#
# float diameter, cylinder diameter, m
#  length, cylinder length, m
#  Tair, air temperature, K
#  Pair, barometric pressure, mb
#  speed; fluid (wind) speed, m/s
def h_cylinder_in_air(
        diameter: float,
        length: float,
        t_air: float,
        p_air: float,
        speed: float,
) -> float:
        a = 0.56  # parameters from Bedingfield and Drew
        b = 0.281
        c = 0.4

        density = p_air * 100. / ( R_AIR * t_air );
        Re = np.max([speed, MIN_SPEED]) * density * diameter / viscosity(t_air);
        Nu = b * np.power(Re,(1. - c)) * np.power(Pr,(1. - a));
        return (Nu * thermal_cond(t_air) / diameter);


# /* ============================================================================
#  * Purpose: to calculate the convective heat transfer coefficient, W/(m2 K)
#  *          for flow around a sphere.
#  *
#  * Reference: Bird, Stewart, and Lightfoot (BSL), page 409.
#  *
#  */
def h_sphere_in_air(diameter: float, t_air: float, p_air: float, speed: float) -> float:
    density = p_air * 100. / ( R_AIR * t_air )
    Re = max(speed, MIN_SPEED) * density * diameter / viscosity(t_air)
    Nu = 2.0 + 0.6 * np.sqrt(Re) * np.power(Pr, 0.3333)
    return(Nu * thermal_cond(t_air) / diameter)


# /* ============================================================================
#  *  Purpose: calculate the atmospheric emissivity.
#  *
#  *  Reference: Oke (2nd edition), page 373.
#  */
# float Tair,	/* air temperature, K */
# rh; /* relative humidity, fraction between 0 and 1 */
# no test
def emis_atm(t_air: float, rh: float) -> float:
    e = rh * esat(t_air, 0)
    return( 0.575 * np.power(e, 0.143))


def daynum(year: int, month: int, day: int) -> float:
    begmonth = np.array([0,0,31,59,90,120,151,181,212,243,273,304,334])
    # begmonth[0] is dummy

    # /* There is no year 0 in the Gregorian calendar and the leap year cycle
    #  * changes for earlier years. */
    if year < 1:
      return -1

    # /* Leap years are divisible by 4, except for centurial years not divisible
    #  * by 400. */

    if ( ((year%4) == 0 and (year%100) != 0) or (year%400) == 0):
      leapyr = 1
    else:
      leapyr = None

    dnum = begmonth[month] + day

    if (leapyr and (month > 2)):
      dnum += 1

    return dnum

