import numpy as np
import matplotlib
import random
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
from math import cos, acos, pi, sin
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

tree = ET.parse("maps/manhattan-map.osm")
root = tree.getroot()
ways = [x for x in root.findall("way") if is_road(x)]
nodeset = set()
for way in ways:
    for node in way.findall("nd"):
        nodeset.add(node.get("ref"))
nodedict = {}
for item in nodeset:
    nodedict[item] = []
for way in ways:
    l = way.findall("nd")
    for index in range(len(l)-1):
        nodedict[l[index].get("ref")].append(l[index+1].get("ref"))
# i = nodeset.pop()
# while(len(nodedict[i]) <3):
#     i = nodeset.pop()
sum = 0
for node in nodeset:
    sum +=1
print(sum)
dict = {}
nodes = root.findall("node")
for item in nodes:
    dict[item.get("id")] = (item.get("lat"), item.get("lon"))
newdict = {(dict[item], 1):[dict[x] for x in nodedict[item]] for item in nodedict}
lat = [0]*sum
lon = [0]*sum
index = 0
for key in newdict:
    lat[index] = key[0][0]
    lon[index] = key[0][1]
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