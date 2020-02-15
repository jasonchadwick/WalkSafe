import util
import crime_cost as cc

def closestNode(coord, nodeDict):
    nodes = nodeDict.keys()
    bestDist = None
    bestNode = None
    for node in nodes:
        dist = util.getDist(coord, node)
        if bestNode == None:
            bestNode = node
            bestDist = dist
        elif dist < bestDist:
            bestNode = node
            bestDist = dist
        
    return bestNode
        
print("facs")
nodes = cc.update(cc.getNodedata())
print("true")
print(closestNode((40.7, -74.0), nodes))