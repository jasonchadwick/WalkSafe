from crime_cost import *
import json

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
for datapoint in nodeData:
    finaldict[(datapoint[0], datapoint[1])] = calcRisk.calcRisk((float(datapoint[0]), float(datapoint[1])), averageNodeDict)
    if count %20000 == 0:
        print(count)
    count+=1
print("finished doing crime")
#make coords into strings and store in json
stringdict = {}
for node in finaldict.keys():
    stringdict[str(node[0]) + " " + str(node[1])] = finaldict[node]
json.dump(stringdict, open("data/nodetimerisk.json","w"))
nodelist = searchProblem.getRoute(nodeData, finaldict, 15, [key for key in nodeData][random.randint(0,len(nodeData))], [key for key in nodeData][random.randint(0,len(nodeData))])
coordlist = []
for coord in nodelist:
    coordlist.append([coord[0],coord[1]])
#plotdata(importantcrimeData)