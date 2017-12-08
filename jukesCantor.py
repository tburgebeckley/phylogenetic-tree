import math
import time
import Needleman_wunsch as nw
from collections import OrderedDict
import sys

#jukesCantor: implementation of the JukesCantor Distance Alg
#params: s1 (aligned nucleotide sequence), s2 (aligned nucleotide sequence)
#output: numeric value representing evolutionary distance
def jukesCantor(s1, s2):
    diffCtr = 0.0
    lenCtr = 0.0

    for i in range (len(s1)):
        if ((s1[i] != '-') and (s2[i] != '-')):
            lenCtr = lenCtr + 1
            if (s1[i] != s2[i]):
                diffCtr = diffCtr + 1
    diffCtr = float(diffCtr/lenCtr)

    jukes = (-3.0/4 * math.log(1.0-(4.0/3 * diffCtr)))

    return jukes

def prettyPrint(s1, s2, width):
    curIndex = 0
    res = ""
    pretty = "seq1: {}  \t{}\t{}\nseq2: {}  \t{}\t{}\n"
    while len(s1) > 0:
        if len(s1) < width:
            width = len(s1)
        seg1 = s1[0:width]
        seg2 = s2[0:width]

        res += pretty.format(curIndex, seg1, curIndex+width-1,curIndex, seg2, curIndex+width-1)
        s1 = s1[curIndex:]
        s2 = s2[curIndex:]
        curIndex = curIndex + width

    return res

def alignNucleotides(seq1, seq2):
    nw.seq1 = seq1
    nw.seq2 = seq2

    mat, pos = nw.build_matrix(len(seq1) + 1, len(seq2)+1)
    seq1align, seq2align = nw.traceback(mat, pos)

    return seq1align, seq2align

class distanceMatrix:
    #do stuff here to build the matrix
    """A class representing the distance matrix of a collection of aligned strings"""

    def __init__(self):
        self.sequences = OrderedDict()
        self.matrix = OrderedDict()
        self.nameMap = {}

    def readFasta(self, filename):
        lines = []
        with open (filename, "r") as seqs:
            lines = seqs.readlines()

        curChar = 'a'
        for i in range(0,len(lines),2):
            self.sequences[lines[i][1:-1]] = lines[i+1][:-1]
            self.nameMap[lines[i][1:-1]] = curChar
            curChar = chr(ord(curChar)+1)

        return

    def buildMatrix(self):
        for name in self.sequences:
            arr = OrderedDict()
            seq1 = self.sequences[name]
            for name2 in self.sequences:
                if name == name2:
                    arr[name2] = 0
                else:
                    # if name2 in self.matrix and name in self.matrix[name2]:
                    #     arr[name2] = float(self.matrix[name2][name])
                    # else:
                    seq2 = self.sequences[name2]

                    if name2 in self.matrix:
                         aligned_seq1, aligned_seq2 = alignNucleotides(seq2, seq1)
                    else:
                        aligned_seq1, aligned_seq2 = alignNucleotides(seq1, seq2)

                    dist = jukesCantor(aligned_seq1, aligned_seq2)
                    if (dist < 0) : dist = dist * -1.0

                    arr[self.nameMap[name2]] = dist
            self.matrix[self.nameMap[name]] = arr
        return

    def matString(self):
        string = ""
        count = 0
        for name in self.matrix:
            dist = self.matrix[name]
            string += name + " "
            for name in dist:
                string += str(dist[name]) + " "
            string = string[:-1] + '\n'
            count += 1
        return str(count) + '\n' + string[:-1]

    def nameMapString(self):
        string = ""
        for name, value in self.nameMap.items():
            string += "{}=> {}\n".format(name, value)
        return string[:-1]

def main(args):
    if len(args) < 2:
        print("Error: improper arguments supplied\nUsage: python3 jukesCantor.py [inputFile]")
        exit(1)
    else:
        try:
            fo = open(args[1], 'r')
            fo.close()
        except OSError:
            print("Error!", args[1], " was not found!")
            sys.exit(1)


    mat = distanceMatrix()

    mat.readFasta(args[1])
    #begin capturing timing data here
    start_time = time.clock()
    mat.buildMatrix()
    print("Total ALIGNMENT runtime was %s seconds:" % (time.clock() - start_time))

    #end capturing timing data
    outfile = args[1] + ".dist"
    names = args[1] + ".names"

    fp = open(outfile, 'w+')
    fp.write(mat.matString())
    fp.close()

    fp = open(names, 'w+')
    fp.write(mat.nameMapString())
    fp.close()

if __name__ == "__main__":
    main(sys.argv)
