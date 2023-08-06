import numpy as np

from wbgt.helper import (
    h_sphere_in_air,
    emis_atm,
    viscosity,
    diffusivity,
    evap,
    dew_point,
    h_cylinder_in_air,
    esat,
    stab_srdt,
    est_wind_speed,

    STEFANB,
    D_WICK,
    L_WICK,
    EMIS_WICK,
    ALB_WICK,
    R_AIR,
    RATIO,
    Pr,
    REF_HEIGHT,
)

from wbgt.solar import (
    calc_solar_parameters,
)

CONVERGENCE = 0.02
EMIS_SFC = 0.999
EMIS_GLOBE = 0.95
ALB_SFC = 0.45
ALB_GLOBE = 0.05
MAX_ITER = 50
D_GLOBE = 0.0508
PI = np.pi

def t_globe(
        t_air: float,
        rh: float,
        p_air: float,
        speed: float,
        solar: float,
        fdir: float,
        cza: float
) -> float:
    Tsfc = t_air;
    Tglobe_prev = t_air
    # /* first guess is the air temperature */
    converged = False;
    counter = 0;

    while not converged and counter < MAX_ITER:
        counter += 1
        Tref = 0.5 * (Tglobe_prev + t_air)
        # /* evaluate properties at the average temperature */
        h = h_sphere_in_air(D_GLOBE, Tref, p_air, speed)

        b = 0.5 * (emis_atm(t_air, rh) * np.power(t_air, 4.) + EMIS_SFC*np.power(Tsfc, 4.)) - h/(STEFANB*EMIS_GLOBE)*(Tglobe_prev - t_air) + solar/(2. * STEFANB * EMIS_GLOBE) * (1. - ALB_GLOBE) * (fdir * (1./(2. * cza) - 1.) + 1. + ALB_SFC)
        Tglobe_new = np.power(b, 0.25)

        if np.fabs(Tglobe_new-Tglobe_prev) < CONVERGENCE:
            converged = True;

        Tglobe_prev = 0.9 * Tglobe_prev + 0.1 * Tglobe_new

    if converged:
        return Tglobe_new - 273.15
    else:
        raise 'cannot calc Tglobe'
        # return (-9999.);


# /* ============================================================================
#  *  Purpose: to calculate the natural wet bulb temperature.
#  *
#  *  Author:  James C. Liljegren
#  * Decision and Information Sciences Division
#  * Argonne National Laboratory
#  */
# float Tair,/* air (dry bulb) temperature, degC*/
# rh,
# Pair,/* barometric pressure, mb*/
# speed,/* wind speed, m/s*/
# solar,/* solar irradiance, W/m2*/
# fdir,/* fraction of solar irradiance due to direct beam*/
# cza;/* cosine of solar zenith angle*/
# intrad;/* switch to enable/disable radiative heating;
# * no radiative heating --> pyschrometric wet bulb temp*/

def t_wb(
        t_air: float,
        rh: float,
        p_air: float,
        speed: float,
        solar: float,
        fdir: float,
        cza: float,
        rad: int,
) -> float:
    a = 0.56  # /* from Bedingfield and Drew */
    converged = False
    counter = 0

    Tsfc = t_air;
    sza = np.arccos(cza)  #  /* solar zenith angle, radians */
    eair = rh * esat(t_air,0);
    Tdew = dew_point(eair,0);
    Twb_prev = Tdew  # /* first guess is the dew point temperature */

    while not converged and counter < MAX_ITER:
        counter += 1
        Tref = 0.5*( Twb_prev + t_air )  # /* evaluate properties at the average temperature */
        h = h_cylinder_in_air(D_WICK, L_WICK, Tref, p_air, speed)
        Fatm = STEFANB * EMIS_WICK * ( 0.5*( emis_atm(t_air,rh)*np.power(t_air,4.) + EMIS_SFC*np.power(Tsfc,4.) ) - np.power(Twb_prev,4.) ) + (1.-ALB_WICK) * solar * ( (1.-fdir)*(1.+0.25*D_WICK/L_WICK) + fdir*((np.tan(sza)/PI)+0.25*D_WICK/L_WICK) + ALB_SFC )
        ewick = esat(Twb_prev, 0);
        density = p_air * 100. / (R_AIR * Tref);
        Sc = viscosity(Tref)/(density*diffusivity(Tref,p_air));
        Twb_new = t_air - evap(Tref)/RATIO * (ewick-eair)/(p_air-ewick) * np.power(Pr/Sc,a) + (Fatm/h * rad);

        if (np.fabs(Twb_new-Twb_prev) < CONVERGENCE ):
            converged = True


        Twb_prev = 0.9*Twb_prev + 0.1*Twb_new

    if converged:
        return (Twb_new-273.15)
    else:
        raise 'cannot calc t_wb'


def calc_wbgt(
    year: int,
    month: int,
    day: int,
    hour: int,
    minute: int,
    gmt: int,
    avg: int,
    lat: float,
    lon: float,
    solar: float,
    pres: float,
    t_air: float,
    relhum: float,
    speed: float,
    zspeed: float,
    dT: float,
    urban: bool,
    est_speed: float,
) -> float:
    hour_gmt = hour - gmt + ( minute - 0.5 * avg ) / 60.;
    dday = day + hour_gmt / 24.;
    solar, cza, fdir = calc_solar_parameters(year, month, dday, lat, lon, solar)
    print(solar, cza, fdir, zspeed)

    if zspeed != REF_HEIGHT:
        if cza > 0.:
            daytime = True
        else:
            daytime = False
        stability_class = stab_srdt(daytime, speed, solar, dT)
        est_speed = est_wind_speed(speed, zspeed, stability_class, urban)
        speed = est_speed

    # /*
    # *  unit conversions
    # */
    tk = t_air + 273.15  #  /* degC to kelvin */
    rh = 0.01 * relhum  # /* % to fraction  */

    # /*
    # *  calculate the globe, natural wet bulb, psychrometric wet bulb, and
    # *  outdoor wet bulb globe temperatures
    # */
    #
   
    print(tk, rh, pres, speed, solar, fdir, cza)

    Tg   = t_globe(tk, rh, pres, speed, solar, fdir, cza)
    Tnwb = t_wb(tk, rh, pres, speed, solar, fdir, cza, 1)
    Tpsy = t_wb(tk, rh, pres, speed, solar, fdir, cza, 0)
    Twbg = 0.1 * t_air + 0.2 * (Tg) + 0.7 * (Tnwb)

    print(Tg, Tnwb, Tpsy, Twbg)

    return Twbg
