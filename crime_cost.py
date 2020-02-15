import crimeParsing
import numpy as np
import searchProblem
import json
import calcRisk
import matplotlib
import random
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
from math import cos, acos, pi, sin
minlat = 40.683
maxlat = 40.883
minlon = -74.037
maxlon = -73.829
def getNodedata():
    fetcheddict = json.load(open("data.txt"))
    return revertdict(fetcheddict)
def convertkey(t):
    return str(t[0][0]) + " " + str(t[0][1])
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
    return (l[0], l[1])
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
def plotdata(importantcrimeData):
    lat = [0]*len(importantcrimeData)
    lon = [0]*len(importantcrimeData)
    index = 0
    for datapoint in importantcrimeData:
        lat[index] = importantcrimeData[index][0]
        lon[index] = importantcrimeData[index][1]
        index+=1
    lat = lat[0:index]
    lon = lon[0:index]
    rlist1 = [0]*1000
    rlist2 = [0]*1000
    index2 = 0
    for x in range(1000):
        r = random.randint(0,len(lat))
        rlist1[index2] = float(lat[r])
        rlist2[index2] = float(lon[r])
        index2+=1
    lat = np.array(rlist1)#lat[0:100])
    lon = np.array(rlist2)#lon[0:100])
    plt.scatter(lat, lon, alpha=0.5)
    plt.title('Scatter plot')
    plt.xlabel('lat')
    plt.ylabel('lon')
    plt.show()
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
def update(nodeData):
    return {(float(key[0]), float(key[1])):[(float(item[0]), float(item[1])) for item in nodeData[key]] for key in nodeData}
nodeData = getNodedata()
datalist = crimeParsing.load_crimes()
importantcrimeData = [[]]*len(datalist)
for index,datapoint in enumerate(datalist):
    newdatapoint = datapoint.split(" ")
    timelist = newdatapoint[3].split(":")
    importantcrimeData[index] = [float(newdatapoint[0]), float(newdatapoint[1]), float(newdatapoint[2]), [int(timelist[0]), int(timelist[1]), int(timelist[2])]]
averageNodeDict = {}
temp1 = round(minlat,3)
temp2 = round(minlon,3)
while(temp1 <= maxlat):
    while(temp2 <= maxlon):
        averageNodeDict[(round(temp1,3), round(temp2,3))] = []
        temp2 += .001
        temp2 = round(temp2,3)
    temp2 = minlon
    temp1 +=.001
    temp1 = round(temp1, 3)
for datapoint in importantcrimeData:
    averageNodeDict[round(datapoint[0],3),round(datapoint[1],3)].append(datapoint)
max = 0
maxplace = (0,0)
for item in averageNodeDict:
    if len(averageNodeDict[item])> max:
        max = len(averageNodeDict[item])
        maxplace = item
print(maxplace)
nodeData = update(nodeData)
finaldict = {(datapoint[0],datapoint[1]):calcRisk.calcRisk((float(datapoint[0]),float(datapoint[1])), averageNodeDict) for datapoint in nodeData}
searchProblem.getRoute(nodeData, finaldict, 15, [key for key in nodeData][random.randint(0,len(nodeData))], [key for key in nodeData][random.randint(0,len(nodeData))])
plotdata(importantcrimeData)
