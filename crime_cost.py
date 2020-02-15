import crimeParsing
import numpy as np
import json
import matplotlib
import random
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
from math import cos, acos, pi, sin
minlat = 40.683
maxlat = 40.883
minlon = -74.0369999
maxlon = -73.8299999
def getNodedata():
    fetcheddict = json.load(open("data.txt"))
    return revertdict(fetcheddict)
def convertkey(t):
    return str(t[0][0]) + " " + str(t[0][1]) + " " + str(t[1])
def convertval(t):
    return str(t[0]) + " " + str(t[1])
def convertdict(d):
    newd = {}
    for key in d:
        newkey = convertkey(key)
        newval = [convertval(val) for val in d[key]]
        newd[newkey] = newval
    return newd
def revertkey(t):
    l = t.split(" ")
    return ((l[0], l[1]), l[2])
def revertval(v):
    l = v.split(" ")
    return (l[0], l[1])
def revertdict(d):
    newd = {}
    for key in d:
        newkey = revertkey(key)
        newval = [revertval(val) for val in d[key]]
        newd[newkey] = newval
    return newd
def in_range(lat, lon):
  return lat >= minlat and lat <= maxlat and lon >= minlon and lon <= maxlon
def is_road(way):
    for tag in way.findall("tag"):
        if tag.get("k") == "highway":
            return True
    return False
def calcdist(tuple1, tuple2):
    lat1 = tuple1[0]
    lat2 = tuple2[0]
    long1 = tuple1[1]
    long2 = tuple2[1]
    y1 = lat1
    x1 = long1
    y2 = lat2
    x2 = long2
    # all assumed to be in decimal degrees

    # if (and only if) the input is strings
    # use the following conversions

    y1 = float(y1)
    x1 = float(x1)
    y2 = float(y2)
    x2 = float(x2)
    #
    R = 3958.76  # miles = 6371 km
    #
    y1 *= pi / 180.0
    x1 *= pi / 180.0
    y2 *= pi / 180.0
    x2 *= pi / 180.0
    #
    # approximate great circle distance with law of cosines
    #
    return acos(sin(y1) * sin(y2) + cos(y1) * cos(y2) * cos(x2 - x1)) * R
nodeData = getNodedata()
crimeData = crimeParsing.load_crimes()
crimeData = [datapoint.split(" ") for datapoint in crimeData]
importantcrimeData = [datapoint for datapoint in crimeData if in_range(float(datapoint[0]), float(datapoint[1]))]
print(len(importantcrimeData))



