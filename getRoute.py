import json
import searchProblem
import random
import crime_cost
import matplotlib.pyplot as plt
import startlogic

def getRoute(start, end, nodeDict):
  start1 = startlogic.closestNode(start, nodeDict)
  end1 = startlogic.closestNode(end, nodeDict)
  nodes = json.load(open("data/nodetimerisk.json"))
  tuplenodes = {}
  for n in nodes.keys():
    tup = (float(n.split()[0]), float(n.split()[1]))
    minidict = nodes[n]
    newmini = {}
    for mini in minidict.keys():
      newmini[int(mini)] = minidict[mini]
    tuplenodes[tup] = newmini
  nodeData = crime_cost.update(crime_cost.getNodedata())
  print("starting search")
  nodelist = searchProblem.getRoute(nodeData, tuplenodes, 15, start1, end1)
  print("finished search")
  coordlist = []
  for coord in nodelist:
      coordlist.append([coord[0],coord[1]])
  print(coordlist)
  while(len(coordlist)>50):
    count = 0
    newlist = []
    for coord in coordlist:
      if count%2 == 0 or count == len(coordlist) - 1:
        newlist.append(coordlist[count])
      count += 1
    coordlist = newlist
  json.dump({"locations":coordlist}, open("locations.json", "w"))

stuff=[(40.8293935, -73.8754458), (40.8295914, -73.874754), (40.8296024, -73.8747154),
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

#coordlist = []
#for coord in stuff:
#    coordlist.append([coord[0],coord[1]])
#print(coordlist)
#while(len(coordlist)>50):
#  count = 0
#  newlist = []
#  for coord in coordlist:
#    if count%2 == 0 or count == len(coordlist) - 1:
#      newlist.append(coordlist[count])
#    count += 1
#  coordlist = newlist
#json.dump({"locations":coordlist}, open("locations1.json", "w"))

stuf = json.load(open("data.txt"))
newd = {}
for s in stuf.keys():
  parsed = s.split()
  minil = []
  for ss in stuf[s]:
    pars = s.split()
    minil.append((pars[0],pars[1]))
  newd[(s[0],s[1])] = minil
#getRoute((40.73500827774132,-73.99870871510616),(40.776192757644445,-73.95197656436147),newd)

print(startlogic.closestNode((40.73500827774132,-73.99870871510616), newd))