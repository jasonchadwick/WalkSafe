# import xml.etree.ElementTree as ET

# def is_road(way):
#     for tag in way.findall("tag"):
#         if tag.get("k") == "highway":
#             return True
#     return False

# def get_road_nodes(way):
#     way.findall("nd")

# tree = ET.parse("maps/manhattan-map.osm")
# root = tree.getroot()
# roads = [x for x in root.findall("way") if is_road(x)]

# print(roads[0])

#for way in root.findall("way"):
 #   if way.get("id") == "5668968":
  #      for tag in way.findall("tag"):
   #         if tag.get("k") == "highway":
    #            print(tag.get("v"))
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