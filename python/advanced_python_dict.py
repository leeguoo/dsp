import pandas as pd
from collections import defaultdict

df = pd.read_csv("faculty.csv")

#q6
def getpairs1(x):
    return x[0].split()[-1],[x[1].lstrip(),x[2][:x[2].index('Professor')+9],x[3]]

d = defaultdict(list)
for k, v in list(df.apply(getpairs1,axis=1)):
    d[k].append(v)
print sorted([(k,v) for k,v in d.items()])[:3]
print ""

#q7
def getpairs2(x):
    return (x[0].split()[0],x[0].split()[-1]),[x[1].lstrip(),x[2][:x[2].index('Professor')+9],x[3]]

d = defaultdict(list)
for k, v in list(df.apply(getpairs2,axis=1)):
    d[k].append(v)
print sorted([(k,v) for k,v in d.items()])[:3]
print ""

#q8
ks = d.keys()
print sorted(ks,key=lambda k: k[1])
