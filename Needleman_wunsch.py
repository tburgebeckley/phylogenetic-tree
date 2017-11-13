seq1 = None
seq2 = None
match = 2
mismatch = -1
gap = -1


def build_matrix(rows, cols):
    matrix = [[0 for x in range(cols)] for y in range(rows)]

    for x in range(1,cols):
        matrix[0][x] = matrix[0][x-1] -1
    for y in range(1,rows):
        matrix[y][0] = matrix[y-1][0] -1

    for i in range(1,rows):
        for j in range(1,cols):
            matrix[i][j] = calc_score(matrix, i, j)


    return matrix, (rows-1, cols-1)


def calc_score(mat, x, y):
    similarity = match if seq1[x - 1] == seq2[y - 1] else mismatch

    diag_score = mat[x - 1][y - 1] + similarity
    up_score   = mat[x - 1][y] + gap
    left_score = mat[x][y - 1] + gap

    return max(0, diag_score, up_score, left_score)

def traceback(score_matrix, start_pos):
    i, j = start_pos
    aligned_seq1 = []
    aligned_seq2 = []
    while i > 0 and j > 0:
        score = score_matrix[i][j]
        diag = score_matrix[i-1][j-1]
        up = score_matrix[i][j-1]
        left = score_matrix[i-1][j]

        if score == diag + (match if seq1[i-1] == seq2[j-1] else mismatch):
            aligned_seq1 += seq1[i-1]
            aligned_seq2 += seq2[j-1]
            i-=1
            j-=1
        elif score == left + gap:
            aligned_seq1 += seq1[i-1]
            aligned_seq2 += '-'
            i-=1
        else:
            aligned_seq1 += '-'
            aligned_seq2 += seq2[j-1]
            j-=1
    while i > 0:
        aligned_seq1 += seq1[i-1]
        aligned_seq2 += '-'
        i-=1
    while j > 0:
        aligned_seq1 += '-'
        aligned_seq2 += seq2[j-1]
        j-=1       

    return ''.join(reversed(aligned_seq1)), ''.join(reversed(aligned_seq2))