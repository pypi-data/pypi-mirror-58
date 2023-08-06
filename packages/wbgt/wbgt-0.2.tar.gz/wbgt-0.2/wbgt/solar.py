import numpy as np

from wbgt.helper import (
    daynum
)


TWOPI = 2 * np.pi;
DEG_RAD = 0.017453292519943295
RAD_DEG = 57.295779513082323

# define physical constants
SOLAR_CONST = 1367.


# computational and physical limits
CZA_MIN = 0.00873
NORMSOLAR_MAX = 0.85

# ============================================================================
#  Version 3.0 - February 20, 1992.

#  solarposition() employs the low precision formulas for the Sun's coordinates
#  given in the "Astronomical Almanac" of 1990 to compute the Sun's apparent
#  right ascension, apparent declination, altitude, atmospheric refraction
#  correction applicable to the altitude, azimuth, and distance from Earth.
#  The "Astronomical Almanac" (A. A.) states a precision of 0.01 degree for the
#  apparent coordinates between the years 1950 and 2050, and an accuracy of
#  0.1 arc minute for refraction at altitudes of at least 15 degrees.

#  The following assumptions and simplifications are made:
#  -> refraction is calculated for standard atmosphere pressure and temperature
#     at sea level.
#  -> diurnal parallax is ignored, resulting in 0 to 9 arc seconds error in
#     apparent position.
#  -> diurnal aberration is also ignored, resulting in 0 to 0.02 second error
#     in right ascension and 0 to 0.3 arc second error in declination.
#  -> geodetic site coordinates are used, without correction for polar motion
#     (maximum amplitude of 0.3 arc second) and local gravity anomalies.
#  -> local mean sidereal time is substituted for local apparent sidereal time
#     in computing the local hour angle of the Sun, resulting in an error of
#     about 0 to 1 second of time as determined explicitly by the equation of
#     the equinoxes.

#  Right ascension is measured in hours from 0 to 24, and declination in
#  degrees from 90 to -90.
#  Altitude is measured from 0 degrees at the horizon to 90 at the zenith or
#  -90 at the nadir. Azimuth is measured from 0 to 360 degrees starting at
#  north and increasing toward the east at 90.
#  The refraction correction should be added to the altitude if Earth's
#  atmosphere is to be accounted for.
#  Solar distance from Earth is in astronomical units, 1 a.u. representing the
#  mean value.

#  The necessary input parameters are:
#  -> the date, specified in one of three ways:
#       1) year, month, day.fraction
#       2) year, daynumber.fraction
#       3) days.fraction elapsed since January 0, 1900.
#  -> site geodetic (geographic) latitude and longitude.

#  Refer to the function declaration for the parameter type specifications and
#  formats.

#  solarposition() returns -1 if an input parameter is out of bounds, or 0 if
#  values were written to the locations specified by the output parameters.


#  Author: Nels Larson
#          Pacific Northwest National Laboratory
#          P.O. Box 999
#          Richland, WA 99352
#          U.S.A.

# int    year,          /* Four digit year (Gregorian calendar).
#                        *   [1950 through 2049; 0 o.k. if using days_1900] */
#        month;         /* Month number.
#                        *   [1 through 12; 0 o.k. if using daynumber for day] */
# double day,           /* Calendar day.fraction, or daynumber.fraction.
#                        *   [If month is NOT 0:
#                        *      0 through 32; 31st @ 18:10:00 UT = 31.75694
#                        *    If month IS 0:
#                        *      0 through 367; 366 @ 18:10:00 UT = 366.75694] */
#        days_1900,     /* Days since 1900 January 0 @ 00:00:00 UT.
#                        *   [18262.0 (1950/01/00) through 54788.0 (2049/12/32);
#                        *    1990/01/01 @ 18:10:00 UT = 32873.75694;
#                        *    0.0 o.k. if using {year, month, day} or
#                        *    {year, daynumber}] */
#        latitude,      /* Observation site geographic latitude.
#                        *   [degrees.fraction, North positive] */
#        longitude,     /* Observation site geographic longitude.
#                        *   [degrees.fraction, East positive] */
#        *ap_ra,        /* Apparent solar right ascension.
#                        *   [hours; 0.0 <= *ap_ra < 24.0] */
#        *ap_dec,       /* Apparent solar declination.
#                        *   [degrees; -90.0 <= *ap_dec <= 90.0] */
#        *altitude,     /* Solar altitude, uncorrected for refraction.
#                        *   [degrees; -90.0 <= *altitude <= 90.0] */
#        *refraction,   /* Refraction correction for solar altitude.
#                        * Add this to altitude to compensate for refraction.
#                        *   [degrees; 0.0 <= *refraction] */
#        *azimuth,      /* Solar azimuth.
#                        *   [degrees; 0.0 <= *azimuth < 360.0, East is 90.0] */
#        *distance;     /* Distance of Sun from Earth (heliocentric-geocentric).
#                        *   [astronomical units; 1 a.u. is mean distance] */


def solarposition(
        year: int,
        month: int,
        day: float,
        latitude: float,
        longitude: float,
):
    pressure = 1013.25 # /* Earth mean atmospheric pressure at sea level in millibars. */
    temp = 15.0 # /* Earth mean atmospheric temperature at sea level in degrees Celsius. */

    if (latitude < -90.0 or latitude > 90.0 or longitude < -180.0 or longitude > 180.0):
        raise 'coordination is out of range'

    if month != 0:
       daynumber = daynum(year, month, int(day))
    else:
       daynumber = int(day)

    # /* Construct Julian centuries since J2000 at 0 hours UT of date,
    #  * days.fraction since J2000, and UT hours.
    #  */
    delta_years = year - 2000;
    # /* delta_days is days from 2000/01/00 (1900's are negative). */
    delta_days = delta_years * 365 + delta_years / 4 + daynumber;
    if year > 2000:
        delta_days += 1;
    # /* J2000 is 2000/01/01.5 */
    days_J2000 = delta_days - 1.5;

    cent_J2000 = days_J2000 / 36525.0;

    ut, _ = np.modf(day);
    days_J2000 += ut;
    ut *= 24.0;

    mean_anomaly = (357.528 + 0.9856003 * days_J2000);
    mean_longitude = (280.460 + 0.9856474 * days_J2000);

    # /* Put mean_anomaly and mean_longitude in the range 0 -> 2 pi. */
    mean_anomaly, _ = np.modf(mean_anomaly / 360.0)
    mean_anomaly *= TWOPI

    mean_longitude, _ = np.modf(mean_longitude / 360.0)
    mean_longitude *= TWOPI

    mean_obliquity = (23.439 - 4.0e-7 * days_J2000) * DEG_RAD
    ecliptic_long = (
        (1.915 * np.sin(mean_anomaly)) + (0.020 * np.sin(2.0 * mean_anomaly))
    ) * DEG_RAD + mean_longitude

    distance = 1.00014 - 0.01671 * np.cos(mean_anomaly) - 0.00014 * np.cos(2.0 * mean_anomaly);

    # /* Tangent of ecliptic_long separated into sine and cosine parts for ap_ra. */
    ap_ra = np.arctan2(np.cos(mean_obliquity) * np.sin(ecliptic_long), np.cos(ecliptic_long));

    # /* Change range of ap_ra from -pi -> pi to 0 -> 2 pi. */
    if ap_ra < 0.0:
        ap_ra += TWOPI;

    # /* Put ap_ra in the range 0 -> 24 hours. */
    ap_ra, _ = np.modf(ap_ra / TWOPI)
    ap_ra *= 24.0

    ap_dec = np.arcsin(np.sin(mean_obliquity) * np.sin(ecliptic_long));


    gmst0h = 24110.54841 + cent_J2000 * (8640184.812866 + cent_J2000 * (0.093104 - cent_J2000 * 6.2e-6));
    # /* Convert gmst0h from seconds to hours and put in the range 0 -> 24. */
    gmst0h, _ = np.modf(gmst0h / 3600.0 / 24.0)
    gmst0h *= 24.0

    if gmst0h < 0.0:
        gmst0h += 24.0

    # /* Ratio of lengths of mean solar day to mean sidereal day is 1.00273790934
    #  * in 1990. Change in sidereal day length is < 0.001 second over a century.
    #  * A. A. 1990, B6.
    #  */
    lmst = gmst0h + (ut * 1.00273790934) + longitude / 15.0
    # /* Put lmst in the range 0 -> 24 hours. */
    lmst, _ = np.modf(lmst / 24.0)
    lmst *= 24.0

    if lmst < 0.0:
        lmst += 24.0


    local_ha = lmst - ap_ra
    # /* Put hour angle in the range -12 to 12 hours. */

    if local_ha < -12.0:
        local_ha += 24.0
    elif local_ha > 12.0:
        local_ha -= 24.0

    # /* Convert latitude and local_ha to radians. */
    latitude *= DEG_RAD;
    local_ha = local_ha / 24.0 * TWOPI;

    cos_apdec = np.cos(ap_dec);
    # /* Horner's method of polynomial exponent expansion used for gmst0h. */
    sin_apdec = np.sin(ap_dec);
    cos_lat = np.cos(latitude);
    sin_lat = np.sin(latitude);
    cos_lha = np.cos(local_ha);

    altitude = np.arcsin(sin_apdec * sin_lat + cos_apdec * cos_lha * cos_lat);

    cos_alt = np.cos(altitude);

    # /* Avoid tangent overflow at altitudes of +-90 degrees.
    # * 1.57079615 radians is equal to 89.99999 degrees.
    # */

    if np.fabs(altitude) < 1.57079615:
      tan_alt = np.tan(altitude)
    else:
      tan_alt = 6.0e6

    cos_az = (sin_apdec * cos_lat - cos_apdec * cos_lha * sin_lat) / cos_alt;
    sin_az = -(cos_apdec * np.sin(local_ha) / cos_alt);
    azimuth = np.arccos(cos_az);

    # /* Change range of azimuth from 0 -> pi to 0 -> 2 pi. */
    if (np.arctan2(sin_az, cos_az) < 0.0):
        azimuth = TWOPI - azimuth

    # /* Convert ap_dec, altitude, and azimuth to degrees. */

    ap_dec *= RAD_DEG;
    altitude *= RAD_DEG;
    azimuth *= RAD_DEG;

    # /* Compute refraction correction to be added to altitude to obtain actual
    #  * position.
    #  * Refraction calculated for altitudes of -1 degree or more allows for a
    #  * pressure of 1040 mb and temperature of -22 C. Lower pressure and higher
    #  * temperature combinations yield less than 1 degree refraction.
    #  * NOTE:
    #  * The two equations listed in the A. A. have a crossover altitude of
    #  * 19.225 degrees at standard temperature and pressure. This crossover point
    #  * is used instead of 15 degrees altitude so that refraction is smooth over
    #  * the entire range of altitudes. The maximum residual error introduced by
    #  * this smoothing is 3.6 arc seconds at 15 degrees. Temperature or pressure
    #  * other than standard will shift the crossover altitude and change the error.
    #  */

    if altitude < -1.0 or tan_alt == 6.0e6:
      refraction = 0.0;
    else:
      if altitude < 19.225:
        refraction = (0.1594 + (altitude) * (0.0196 + 0.00002 * (altitude))) * pressure
        refraction /= (1.0 + (altitude) * (0.505 + 0.0845 * (altitude))) * (273.0 + temp)
      else:
        refraction = 0.00452 * (pressure / (273.0 + temp)) / tan_alt
  # /*
  #  *  to match Michalsky's sunae program, the following line was inserted
  #  *  by JC Liljegren to add the refraction correction to the solar altitude
  #  */
    altitude = altitude + refraction;

#        *ap_ra,        /* Apparent solar right ascension.
#                        *   [hours; 0.0 <= *ap_ra < 24.0] */
#        *ap_dec,       /* Apparent solar declination.
#                        *   [degrees; -90.0 <= *ap_dec <= 90.0] */
#        *altitude,     /* Solar altitude, uncorrected for refraction.
#                        *   [degrees; -90.0 <= *altitude <= 90.0] */
#        *refraction,   /* Refraction correction for solar altitude.
#                        * Add this to altitude to compensate for refraction.
#                        *   [degrees; 0.0 <= *refraction] */
#        *azimuth,      /* Solar azimuth.
#                        *   [degrees; 0.0 <= *azimuth < 360.0, East is 90.0] */
#        *distance;     /* Distance of Sun from Earth (heliocentric-geocentric).
#                        *   [astronomical units; 1 a.u. is mean distance] */
    return (ap_ra, ap_dec, altitude, refraction, azimuth, distance)


# /* ============================================================================
#  *  Purpose: to calculate the cosine solar zenith angle and the fraction of the
#  *     solar irradiance due to the direct beam.
#  *
#  *  Author:  James C. Liljegren
#  *     Decision and Information Sciences Division
#  *     Argonne National Laboratory
#  */
# int  year,    /* 4-digit year, e.g., 2007              */
#   month;  /* 2-digit month; month = 0 implies day = day of year      */

# double day;    /* day.fraction of month if month > 0;
#          else day.fraction of year if month = 0 (GMT)        */
# float  lat,    /* north latitude                  */
#   lon,    /* east latitude (negative in USA)            */
#   *solar,  /* solar irradiance (W/m2)              */
#   *cza,    /* cosine of solar zenith angle            */
#   *fdir;  /* fraction of solar irradiance due to direct beam      */
def calc_solar_parameters(
        year: int,
        month: int,
        day: int,
        lat: float,
        lon: float,
        solar: float,
) -> (float, float, float):
    # -> solar, cza, fdir

    ap_ra, ap_dec, elev, refr, azim, soldist = solarposition(
        year, month, day, lat, lon,
    )

    cza = np.cos( (90.-elev)*DEG_RAD );
    toasolar = SOLAR_CONST * np.max([0., cza]) / (soldist*soldist)
    # /*
    #  *  if the sun is not fully above the horizon
    #  *  set the maximum (top of atmosphere) solar = 0
    #  */

    if cza < CZA_MIN:
        toasolar = 0.

    if toasolar > 0.:
        # /*
        # *  account for any solar sensor calibration errors and
        # *  make the solar irradiance consistent with normsolar
        # */
        normsolar = np.min([solar/toasolar, NORMSOLAR_MAX])
        solar = normsolar * toasolar
        # /*
        # *  calculate the fraction of the solar irradiance due to the direct beam
        # */
        if normsolar > 0.:
            fdir = np.exp( 3. - 1.34 * normsolar - 1.65 / normsolar )
            fdir = max(min(fdir, 0.9), 0.0)
        else:
            fdir = 0.
    else:
        fdir = 0.

    return (solar, cza, fdir)
