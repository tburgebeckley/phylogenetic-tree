#!usr/bin/python3
import sys

#Initialization - Read in data and build nested hash structures
if len(sys.argv) > 2:
    print("Error, only a single filename may be passed as an arguemnt.")
    print("Usage: python3 agglomeritiveCluster.py inputfilename.txt")
else:
    try:
        fo = open(sys.argv[1], 'r')
        print("File " + sys.argv[1] + " was successfully opened!")
    except OSError:
        print("Error!", sys.argv[1], " was not found!")

numSeq = int(fo.readline())
clusterNames = []
distances = []

for line in fo:
    parse = line.split( )
    clusterNames.append(parse[0])
    distances.append(parse[1:])

originalDist = {}
clusterDist = {}

#Create inner dict
for i in range(0, numSeq):
    innerDict = {}
    for j in range(0, numSeq):
        innerDict[clusterNames[j]] = distances[i][j]
    print(innerDict)
    originalDist[clusterNames[i]] = innerDict
for key in originalDist:
    print(key, " ", originalDist[key])
#STEP 1: Cluster
