from crime_cost import *
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
def plotdata(importantcrimeData, nodeData):
    nodelist = [(40.8293935, -73.8754458), (40.8295914, -73.874754), (40.8296024, -73.8747154),
                (40.8296199, -73.8746368), (40.8296368, -73.8745611), (40.8296692, -73.8744553),
                (40.8298634, -73.8738199), (40.8298782, -73.8737574), (40.8298988, -73.8736705),
                (40.8300158, -73.8732656), (40.8301185, -73.8729005), (40.8301526, -73.8727854),
                (40.8301932, -73.8726486), (40.8300694, -73.872612), (40.8302791, -73.8718838), (40.830305, -73.871794),
                (40.8303298, -73.8717088), (40.8303984, -73.8714714), (40.830563, -73.870903), (40.83082, -73.870007),
                (40.8307071, -73.869981), (40.8307306, -73.8698986), (40.8309379, -73.8691664),
                (40.8309415, -73.8691538), (40.8296207, -73.8688446), (40.8296314, -73.8687372),
                (40.8296433, -73.8686351), (40.8297441, -73.8678657), (40.8297584, -73.8677786),
                (40.8297736, -73.8676861), (40.8298695, -73.8669269), (40.8298777, -73.8668544),
                (40.8298086, -73.8668384), (40.8297603, -73.8668273), (40.8277753, -73.8663679), (40.82768, -73.866346),
                (40.8277891, -73.8655176), (40.827802, -73.86542), (40.8278154, -73.8653197), (40.827926, -73.864494),
                (40.8280101, -73.8638635), (40.8280366, -73.8636648), (40.828049, -73.863572),
                (40.8280596, -73.8634906), (40.828158, -73.862734), (40.8281766, -73.8626474),
                (40.8281872, -73.8625694), (40.8282857, -73.8617924), (40.8283026, -73.8617224),
                (40.8283056, -73.8616352), (40.8284031, -73.8608086), (40.828419, -73.860674),
                (40.8284358, -73.8605363), (40.8285382, -73.8596999), (40.828548, -73.85962), (40.8285595, -73.8595343),
                (40.8284956, -73.8595055), (40.8279253, -73.859252), (40.8282841, -73.8566163),
                (40.8283014, -73.8565085), (40.8283105, -73.8563991), (40.8284202, -73.8555863),
                (40.8286898, -73.8535448), (40.8286259, -73.8535314), (40.8285734, -73.8535158),
                (40.8279661, -73.8533909), (40.8279038, -73.8533742), (40.827919, -73.853261), (40.827933, -73.8531571),
                (40.827887, -73.8531443), (40.82727, -73.8529941)]
    list1 = np.array([item[0] for item in nodelist])
    list2 = np.array([item[1] for item in nodelist])  # lon[0:100])
    max1 = np.amax(list1)
    max2 = np.amax(list2)
    min1 = np.amin(list1)
    min2 = np.amin(list2)
    lat = [0] * len(nodeData)
    lon = [0] * len(nodeData)
    index = 0
    for datapoint in nodeData:
        lat[index] = datapoint[0]
        lon[index] = datapoint[1]
        index += 1
    lat = lat[0:index]
    lon = lon[0:index]
    rlist1 = [0] * 1000
    rlist2 = [0] * 1000
    index2 = 0
    while index2 < 1000:
        r = random.randint(0, len(lat) - 1)
        guess1 = float(lat[r])
        guess2 = float(lon[r])
        if min1 <= guess1 and max1 >= guess1 and min2 <= guess2 and max2 >= guess2:
            rlist1[index2] = float(lat[r])
            rlist2[index2] = float(lon[r])
            index2 += 1
    lat2 = np.array(rlist1)  # lat[0:100])
    lon2 = np.array(rlist2)  # lon[0:100])
    plt.scatter(lon2, lat2, alpha=0.5, color = 'r')
    list1 = np.array([item[0] for item in nodelist])
    list2 = np.array([item[1] for item in nodelist])  # lon[0:100])
    max1 = np.amax(list1)
    max2 = np.amax(list2)
    min1 = np.amin(list1)
    min2 = np.amin(list2)
    lat = [0]*len(importantcrimeData)
    lon = [0]*len(importantcrimeData)
    index = 0
    for datapoint in importantcrimeData:
        lat[index] = datapoint[0]
        lon[index] = datapoint[1]
        index+=1
    lat = lat[0:index]
    lon = lon[0:index]
    rlist1 = [0]*1000
    rlist2 = [0]*1000
    index2 = 0
    while index2 < 1000:
        r = random.randint(0,len(lat)-1)
        guess1 = float(lat[r])
        guess2 = float(lon[r])
        if min1 <= guess1 and max1 >= guess1 and min2<= guess2 and max2 >= guess2:
            rlist1[index2] = float(lat[r])
            rlist2[index2] = float(lon[r])
            index2+=1
    lat = np.array(rlist1)#lat[0:100])
    lon = np.array(rlist2)#lon[0:100])
    plt.scatter(lon, lat, alpha=0.5, color = 'b')
    plt.scatter(list2, list1, alpha=0.5, color = "g")
    plt.title('Scatter plot')
    plt.xlabel('lon')
    plt.ylabel('lat')
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
nodenum = len(nodeData)
finaldict = {}
print(nodenum)
count = 0
#for datapoint in nodeData:
#    finaldict[(datapoint[0], datapoint[1])] = calcRisk.calcRisk((float(datapoint[0]), float(datapoint[1])), averageNodeDict)
#    if count %20000 == 0:
#        print(count)
#    count+=1
#print("finished doing crime")
#nodelist = searchProblem.getRoute(nodeData, finaldict, 15, [key for key in nodeData][random.randint(0,len(nodeData))], [key for key in nodeData][random.randint(0,len(nodeData))])
plotdata(nodeData, importantcrimeData)