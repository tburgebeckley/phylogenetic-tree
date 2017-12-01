#!usr/bin/python3
import sys

#Function to return the shortest distance in clusterDist
def minDistInMatrix(clusterDist):
    giftPackage = {'shortestD': float("inf")}
    for key, value in clusterDist.items():
        for innerKey in value:
            if(float(value[innerKey]) > 0 and float(value[innerKey]) < giftPackage['shortestD']):
                giftPackage['shortestD'] = float(value[innerKey])
                giftPackage['shortestOuter'] = key
                giftPackage['shortestInner'] = innerKey
                giftPackage['newClusterName'] = giftPackage['shortestOuter'] + giftPackage['shortestInner']


    return giftPackage

#Function to calculate distances between new cluster and all other cluster
#using single linkage
def singleLinkage(clusterDist, originalDist, clusterNames, giftPackage):
    clusterDist[numSeq-1][giftPackage['newClusterName']] = {}
    clusterDist[numSeq-1][giftPackage['newClusterName']][giftPackage['newClusterName']] = 0
    for cluster in clusterNames:
        dist1 = clusterDist[numSeq][cluster][giftPackage['shortestInner']]
        dist2 = clusterDist[numSeq][cluster][giftPackage['shortestOuter']]
        smallestD = float("inf")
        smallestD = min(float(dist1), float(dist2), smallestD)

        clusterDist[numSeq-1][cluster][giftPackage['newClusterName']] = smallestD
        clusterDist[numSeq-1][giftPackage['newClusterName']][cluster] = smallestD

def printState(cluster, num):
    state = ""
    state +="{} Element Cluster\n".format(num)
    clusters = []
    for item in cluster:
        state += "\t {}".format(item)
        clusters.append(item)
    state += '\n'
    for i in range(len(clusters)):
        state += "{}\t".format(clusters[i])
        for j in range(len(clusters)):
            state += "{}\t".format(cluster[clusters[i]][clusters[j]])
        state += '\n'
    state += '\n'
    print (state)

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
clusterDist[numSeq] = {}

#Create inner dict
for i in range(0, numSeq):
    innerDict = {}
    for j in range(0, numSeq):
        innerDict[clusterNames[j]] = float(distances[i][j])
    originalDist[clusterNames[i]] = dict(innerDict)
    clusterDist[numSeq][clusterNames[i]] = dict(innerDict)

#STEP 1: Cluster
while(numSeq > 2):
    #find which clusters to merge in clusterDist
    giftPackage = minDistInMatrix(clusterDist[numSeq])
    print("Shortest Distance in matrix is: ", giftPackage['shortestD'])
    print("Outer Key: ", giftPackage['shortestOuter'])
    print("Inner Key: ", giftPackage['shortestInner'])
    print("New Cluster Name: ", giftPackage['newClusterName'])
    #merge clusters
    clusterDist[numSeq-1] = {}
    for cluster in clusterDist[numSeq]:
        clusterDist[numSeq-1][cluster] = dict(clusterDist[numSeq][cluster])
    clusterNames.remove(giftPackage['shortestOuter'])
    clusterNames.remove(giftPackage['shortestInner'])
    clusterDist[numSeq-1].pop(giftPackage['shortestOuter'])
    clusterDist[numSeq-1].pop(giftPackage['shortestInner'])
    for cluster in clusterDist[numSeq-1]:
        clusterDist[numSeq-1][cluster].pop(giftPackage['shortestOuter'])
        clusterDist[numSeq-1][cluster].pop(giftPackage['shortestInner'])

    #singleLinkage method called here
    singleLinkage(clusterDist, originalDist, clusterNames, giftPackage)

    clusterNames.append(giftPackage['newClusterName'])
    print("Merging clusters", giftPackage['shortestOuter'], "&", giftPackage['shortestInner'])
    numSeq = numSeq - 1

while (numSeq in clusterDist):
    printState(clusterDist[numSeq], numSeq)
    numSeq += 1