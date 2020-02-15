import xml.etree.ElementTree as ET

tree = ET.parse("maps/manhattan-map.osm")
root = tree.getroot()

for way in root.findall("way"):
    if way.get("id") == "5668968":
        for tag in way.findall("tag"):
            if tag.get("k") == "highway":
                print(tag.get("v"))