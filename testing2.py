import xml.etree.ElementTree as ET

def is_road(way):
    for tag in way.findall("tag"):
        if tag.get("k") == "highway":
           return True
    return False

def get_road_nodes(way):
    way.findall("nd")

tree = ET.parse("maps/manhattan-map.osm")
root = tree.getroot()
roads = [x for x in root.findall("way") if is_road(x)]

print(roads[0])

for way in root.findall("way"):
    if way.get("id") == "5668968":
        for tag in way.findall("tag"):
            if tag.get("k") == "highway":
                print(tag.get("v"))