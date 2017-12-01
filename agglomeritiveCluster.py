#!usr/bin/python3
import sys

#Function to return the shortest distance in clusterDist
def minDistInMatrix(clusterDist):
    giftPackage = {'shortestD': float("inf")}
    for key, value in clusterDist.items():
        for innerKey in value:
            if(float(value[innerKey]) > 0 and float(value[innerKey]) < giftPackage['shortestD']):
                giftPackage['shortestD'] = float(value[innerKey])
                giftPackage['shortestOutter'] = key
                giftPackage['shortestInner'] = innerKey
                giftPackage['newClusterName'] = giftPackage['shortestOutter'] + giftPackage['shortestInner']


    return giftPackage

#Function to calculate distances between new cluster and all other cluster
#using single linkage
def singleLinkage(clusterDist, newClusterName, originalDist, clusterNames):
    for cluster in clusterNames:
        smallestD = float("inf")
        for cluster in clusterNames:


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
    originalDist[clusterNames[i]] = innerDict
    clusterDist[clusterNames[i]] = innerDict

#STEP 1: Cluster
while(numSeq > 2):
    #find which clusters to merge in clusterDist
    giftPackage = minDistInMatrix(clusterDist)
    print("Shortest Distance in matrix is: ", giftPackage['shortestD'])
    print("Outter Key: ", giftPackage['shortestOutter'])
    print("Inner Key: ", giftPackage['shortestInner'])
    print("New Cluster Name: ", giftPackage['newClusterName'])
    #merge clusters
    clusterNames.remove(giftPackage['shortestOutter'])
    clusterNames.remove(giftPackage['shortestInner'])
    clusterDist.pop(giftPackage['shortestOutter'])
    clusterDist.pop(giftPackage['shortestInner'])
    for cluster in clusterDist:
        print(cluster, " ", clusterDist[cluster])

    #singleLinkage method called here
    singleLinkage(clusterDist, giftPackage['newClusterName'], originalDist, clusterNames)

    clusterNames.append(giftPackage['newClusterName'])
    print("Merging clusters", giftPackage['shortestOutter'], "&", giftPackage['shortestInner'])

    numSeq = numSeq - 1
