"""
Shared data for the H2Overflow project.
 
This file defines:
  - FLOOD_THRESHOLDS: "rules of thumb" for what drives a flood
  - SAFE_THRESHOLDS:  conditions that usually mean no flood
  - SAMPLE_STORMS:    storm records (one per street) for evaluation and training
  - TRUE_LABELS:      human labels for each record in SAMPLE_STORMS
 
DATA SCOPE: 4 Miami neighborhoods, 2 representative streets each (8 records).
The two streets per neighborhood are chosen to be spread apart (not adjacent),
so averaging them gives a reading that represents the whole neighborhood rather
than a single block.
 
  Overtown      -> NW 2nd Ave, NW 13th St        (alt: NW 3rd Ave)
  Little Havana -> SW 8th St (Calle Ocho), SW 4th St & 8th Ave
  Brickell      -> Brickell Ave, SW 1st Ave
  Miami Beach   -> Indian Creek Dr, Alton Rd      (alt: Collins Ave, North Bay Rd)
"""
 
# =====================================================================
# HUMAN PART — rules of thumb (IGNORE)
#
# These are NOT used by the ML model. They are the benchmark — a simple
# human-written guide that says "these conditions usually mean a flood."
# We score the ML model against these rules to see if it learned anything
# better than what a person already knows.
# =====================================================================
 
# Conditions that PUSH TOWARD a flood
FLOOD_THRESHOLDS = {
    "heavy_rain_inches":  2.0,   # rain above this starts to matter
    "high_tide_feet":     3.5,   # tide above this backs up drainage
    "low_elevation_feet": 3.0,   # ground below this floods easily
    "soaked_wetness":     0.7,   # ground already this saturated = nowhere for water to go
}
 
# Conditions that PUSH AWAY from a flood
SAFE_THRESHOLDS = {
    "light_rain_inches":   0.5,  # below this, rain rarely floods anything
    "low_tide_feet":       2.5,  # drainage flows freely below this
    "high_elevation_feet": 6.0,  # high ground stays dry
    "dry_wetness":         0.2,  # dry ground absorbs a lot
}
 
 
# =====================================================================
# TASK ASSIGNMENT — real-world data acquisition
#
# Each person owns ONE feature (one column) and retrieves it for ALL 8
# locations below. The placeholder values in SAMPLE_STORMS columns are
# meant to be replaced with real numbers. Do not touch the columns — these
# serve as placeholders for future data you acquire.
#
# Columns: (location, rain_inches, tide_feet, antecedent_wetness, elevation_feet)
#
#   PERSON A  ->  rain_inches        (2nd value in each row)
#                 TRY: NOAA NCEI Climate Data Online  https://www.ncei.noaa.gov/cdo-web/
#                 (local alternative: SFWMD DBHYDRO rainfall stations)
#
#   PERSON B  ->  tide_feet          (3rd value in each row)
#                 TRY: NOAA Tides & Currents, Virginia Key station 8723214
#                 https://tidesandcurrents.noaa.gov/stationhome.html?id=8723214
#
#   PERSON C  ->  antecedent_wetness (4th value in each row, 0.0–1.0)
#                 TRY: NASA SMAP soil moisture, OR compute an Antecedent
#                 Precipitation Index from Person A's rainfall history.
#
#   PERSON D  ->  elevation_feet     (5th value in each row)
#                 TRY: USGS 3DEP / The National Map  https://apps.nationalmap.gov/
#                 (local alternative: Miami-Dade County LiDAR open data)
#
# NOTE: elevation is static (it doesn't change day to day), so Person D only
# needs ONE value per street. Rain, tide, and wetness change over time — Person
# A, B, and C should agree on the SAME dates so the rows line up.
# =====================================================================
 
 
# =====================================================================
# HUMAN PART — starter labeled dataset
#
# Each record is one street under one set of conditions. The values below are
# PLACEHOLDERS (see TASK ASSIGNMENT). Try your best finding real values for
# these locations and dates.
#
# Columns: (location, rain_inches, tide_feet, antecedent_wetness, elevation_feet)
#
# Allowed labels (IGNORE):
#   "flood"     — serious flooding, roads impassable, dispatch immediately
#   "no_flood"  — conditions are safe, no action needed
#   "minor"     — street ponding, passable, worth monitoring
#   "uncertain" — a human couldn't confidently call it either way
# =====================================================================
 
SAMPLE_STORMS = [
    ("Overtown - NW 2nd Ave",               2.7, 2.3, 0.7, 7.0),
    ("Overtown - NW 13th St",               2.4, 2.2, 0.6, 7.5),
    ("Little Havana - SW 8th St",           2.9, 2.5, 0.8, 8.0),
    ("Little Havana - SW 4th St & 8th Ave", 1.2, 2.4, 0.4, 8.5),
    ("Brickell - Brickell Ave",             1.5, 4.2, 0.6, 4.0),
    ("Brickell - SW 1st Ave",               0.8, 3.9, 0.3, 5.0),
    ("Miami Beach - Indian Creek Dr",       0.5, 4.4, 0.5, 3.5),
    ("Miami Beach - Alton Rd",              0.3, 4.0, 0.2, 4.0),
]
 
# Human labels for each record above. (IGNORE)
# PROVISIONAL: these are first-guess labels for the placeholder values. Once the
# real feature data is collected, revisit each label — the correct label depends
# on the actual conditions, so it may change.
TRUE_LABELS = [
    "flood",      # Overtown 2nd Ave:   heavy rain + soaked, poor drainage
    "minor",      # Overtown 13th St:   heavy-ish rain, drains slowly
    "flood",      # Little Havana 8th:  heavy rain + very soaked
    "no_flood",   # Little Havana 4th:  light rain, dry, higher ground
    "flood",      # Brickell Ave:       high tide on low coastal ground
    "minor",      # Brickell 1st Ave:   high tide but slightly higher ground
    "flood",      # Miami Beach Indian Creek: king tide, lowest ground
    "uncertain",  # Miami Beach Alton Rd:     high tide, hard to call
]


# =====================================================================
# ML PART — IGNORE for now
# =====================================================================