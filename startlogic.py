import util

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
        
