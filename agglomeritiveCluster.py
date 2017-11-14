#!usr/bin/python3
import sys


def clusterLinkage(clusterDist, newClusterName, originalDist, clusterNames):
    for name in clusterNames:
        smallest = sys.maxint
        for c1 in name:
            for c2 in newClusterName:
                if originalDist[c1][c2] < smallest:
                    smallestD = originalDist[c1][c2]
        clusterDist[newClusterName][name] = smallest
        clusterDist[cluster][newClusterName] = smallest

def shortestD(clusterD):
    outerkey, innerkey

    return outerkey, innerkey

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

i = 0
for line in fo:
    parse = line.split( )
    clusterNames.append(parse[0])
    for split in parse[1:]:
        print(split, sep=' ', end=' ')
    print()

#STEP 1: Cluster
while len(clusterNames > 2):
    outer, inner = shortestD(clusterDist)