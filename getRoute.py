import json
import searchProblem
import random
import crime_cost
import matplotlib.pyplot as plt

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
nodelist = searchProblem.getRoute(nodeData, tuplenodes, 15, [key for key in nodeData][random.randint(0,len(nodeData))], [key for key in nodeData][random.randint(0,len(nodeData))])
coordlist = []
for coord in nodelist:
    coordlist.append([coord[0],coord[1]])
json.dump({"locations":coordlist}, open("locations.json", "w"))