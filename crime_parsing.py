import xml.etree.ElementTree as ET
import csv
import json

minlat = 40.683
maxlat = 40.883
minlon = -74.0369999
maxlon = -73.8299999

felonies = {'ROBBERY': 0.8, 'PETIT LARCENY': 0.5, 'FELONY ASSAULT': 0.8, 'ASSAULT 3 & RELATED OFFENSES': 0.8, 'HARRASSMENT 2': 0.6, 'GRAND LARCENY': 0.3, 'INTOXICATED & IMPAIRED DRIVING': 0.5, 'RAPE': 1.0, 'DANGEROUS DRUGS': 0.3, 'MURDER & NON-NEGL. MANSLAUGHTER': 1.0, 'KIDNAPPING': 0.9, 'KIDNAPPING & RELATED OFFENSES': 0.9,'DISORDERLY CONDUCT': 0.5, 'INTOXICATED/IMPAIRED DRIVING': 0.5, 'KIDNAPPING AND RELATED OFFENSES': 0.9}

def in_range(lat, lon):
  lat >= minlat and lat <= maxlat and lon >= minlon and lon <= maxlon

crimes = []
with open("data/NYPD_Complaint_YTD.csv") as csvfile:
    rdr = csv.reader(csvfile, delimiter = ",")
    for row in rdr:
      if (row[15] in felonies.keys()):
        crimes.append(' '.join([row[32], row[33], str(felonies[row[15]]), row[4]]))

json.dump(crimes, open("data/crimes.json", "w"))