import math
import numpy as np
import util

def calcRisk(node, crimedict):
  nodelat = node[0]
  nodelon = node[1]
  timedict = {}
  for t in range(24):
    timedict[t] = 1 #change later
  return timedict
  for lat in [nodelat - 0.001, nodelat, nodelat + 0.001]:
    for lon in [nodelon - 0.001, nodelon, nodelon + 0.001]:
      rlat = round(lat,3)
      rlon = round(lon,3)
      crimes = crimedict[(rlat, rlon)]
      for t in range(24):
        for crime in crimes:
          dist = 5280*util.getDist((rlat, rlon), (crime[0],crime[1]))
          hour = crime[3][0]
          minute = crime[3][1]
          timedict[t] += np.exp(-dist*dist/(125000))