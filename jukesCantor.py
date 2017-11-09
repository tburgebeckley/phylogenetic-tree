import math
import SmithWaterman as sm

#jukesCantor: implementation of the JukesCantor Distance Alg
#params: s1 (aligned nucleotide sequence), s2 (aligned nucleotide sequence)
#output: numeric value representing evolutionary distance
def jukesCantor(s1, s2):
    diffCtr = 0;
    lenCtr = 0;

    for i in range (len(s1)):
        if ((s1[i] != '-') or (s2[i] != '-')):
            lenCtr = lenCtr + 1
            if (s1[i] != s2[i]):
                diffCtr = diffCtr + 1
    print (diffCtr)
    diffCtr = float(diffCtr/lenCtr)
    print (lenCtr)
    print (diffCtr)

    jukes = (-3/4 * math.log(1-(4/3 * diffCtr)))

    return jukes

seq1 = "AAAGCTGCAG"
seq2 = "AAGGCTGAGG"
sm.seq1 = seq1
sm.seq2 = seq2

match = 2
mismatch = -1

rows = (len(seq1) +1)
cols = (len(seq2) +1)

score_matrix, start_pos = sm.create_score_matrix(rows, cols)

seq1_aligned, seq2_aligned = sm.traceback(score_matrix, start_pos)

print ('Aligned Sequences:\n\nseq1: {}\nseq2: {}\n'.format(seq1_aligned, seq2_aligned))
print ('jukesCantor distance: {}'.format(jukesCantor(seq1_aligned,seq2_aligned)))
