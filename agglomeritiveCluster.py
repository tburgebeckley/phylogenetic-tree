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
        
#STEP 1: Cluster
