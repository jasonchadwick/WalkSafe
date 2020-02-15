import math
import numpy as np
import util

def calcRiskTest(node, crimedict):
  timedict = {}
  for t in range(24):
    timedict[t] = 1
  return timedict

def calcRisk(node, crimedict):
  nodelat = node[0]
  nodelon = node[1]
  timedict = {}
  for t in range(24):
    timedict[t] = 1
  for lat in [nodelat]:
    for lon in [nodelon]:
  #for lat in [nodelat - 0.001, nodelat, nodelat + 0.001]:
  #  for lon in [nodelon - 0.001, nodelon, nodelon + 0.001]:
      rlat = round(lat,3)
      rlon = round(lon,3)
      crimes = crimedict[(rlat, rlon)]
      for t in range(24):
        for crime in crimes:
          dist = 5280*util.getDist((rlat, rlon), (crime[0],crime[1]))
          hour = crime[3][0]
          minute = crime[3][1]
          dt = min(abs(hour - t), abs(24 - (hour - t)))
          timedict[t] += crime[2] * np.exp(-dist*dist/125000) * np.exp(-dt*dt/18)
  return timedict