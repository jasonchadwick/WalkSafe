import json

def to_tuples(fname):
  f = json.load(open(fname))
  fnew = []
  for i in f:
    fnew.append(i[0],i[1])