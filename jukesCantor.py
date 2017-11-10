import math
import SmithWaterman as sm
from collections import OrderedDict

#jukesCantor: implementation of the JukesCantor Distance Alg
#params: s1 (aligned nucleotide sequence), s2 (aligned nucleotide sequence)
#output: numeric value representing evolutionary distance
def jukesCantor(s1, s2):
    diffCtr = 0
    lenCtr = 0

    for i in range (len(s1)):
        if ((s1[i] != '-') and (s2[i] != '-')):
            lenCtr = lenCtr + 1
            if (s1[i] != s2[i]):
                diffCtr = diffCtr + 1
    diffCtr = float(diffCtr/lenCtr)

    jukes = (-3/4 * math.log(1-(4/3 * diffCtr)))

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
        curIndex = curIndex + width;

    return res;


class distanceMatrix:
    #do stuff here to build the matrix
    """A class representing the distance matrix of a collection of aligned strings"""

    def __init__(self):
        self.sequences = OrderedDict()
        self.matrix = OrderedDict()
    
    def readFasta(self, filename):
        lines = {}
        with open (filename, "r") as seqs:
            lines = seqs.readlines()
        
        for i in range(0,len(lines),2):
            self.sequences[lines[i][1:-1]] = lines[i+1][:-1]

        return
    def buildMatrix(self):
        for name in self.sequences:
            arr = OrderedDict()
            seq1 = self.sequences[name]
            for name2 in self.sequences:
                if name == name2:
                    arr[name2] = 0
                else:
                    seq2 = self.sequences[name2]
                    rows = len(seq1) + 1
                    cols = len(seq2) + 1
                    sm.seq1 = seq1
                    sm.seq2 = seq2

                    score_matrix, start_pos = sm.create_score_matrix(rows, cols)
                    aligned_seq1, aligned_seq2 = sm.traceback(score_matrix, start_pos)

                    dist = jukesCantor(aligned_seq1, aligned_seq2)

                    arr[name2] = dist
            self.matrix[name] = arr
    
    def matString(self):
        string = ""
        
        for name in self.sequences:
            dist = self.matrix[name]
            string += name + " "
            for name in dist:
                string += str(dist[name]) + " "
            string = string[:-1] + '\n'
        return string
            




# rows = (len(seq1) +1)
# cols = (len(seq2) +1)

# 

# seq1_aligned, seq2_aligned = sm.traceback(score_matrix, start_pos)

# print (prettyPrint(seq1_aligned, seq2_aligned,100))
# print ('jukesCantor distance: {}'.format(jukesCantor(seq1_aligned,seq2_aligned)))

mat = distanceMatrix()

mat.readFasta("random.fasta")
mat.buildMatrix()
print (mat.matString())