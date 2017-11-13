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

    max_score = 0
    max_pos = None

    for i in range(1,rows):
        for j in range(1,cols):
            score = calc_score(matrix, i, j)
            if score > max_score:
                max_score = score
                max_pos   = (i, j)

            matrix[i][j] = score

    assert max_pos is not None, 'the x, y position with the highest score was not found'

    return matrix, max_pos


def calc_score(mat, x, y):
    similarity = match if seq1[x - 1] == seq2[y - 1] else mismatch

    diag_score = mat[x - 1][y - 1] + similarity
    up_score   = mat[x - 1][y] + gap
    left_score = mat[x][y - 1] + gap

    return max(0, diag_score, up_score, left_score)

def traceback(score_matrix, start_pos):
    '''Find the optimal path through the matrix.

    This function traces a path from the bottom-right to the top-left corner of
    the scoring matrix. Each move corresponds to a match, mismatch, or gap in one
    or both of the sequences being aligned. Moves are determined by the score of
    three adjacent squares: the upper square, the left square, and the diagonal
    upper-left square.

    WHAT EACH MOVE REPRESENTS
        diagonal: match/mismatch
        up:       gap in sequence 1
        left:     gap in sequence 2
    '''

    END, DIAG, UP, LEFT = range(4)
    aligned_seq1 = []
    aligned_seq2 = []
    x, y         = start_pos
    move         = next_move(score_matrix, x, y)
    while move != END:
        if move == DIAG:
            aligned_seq1.append(seq1[x - 1])
            aligned_seq2.append(seq2[y - 1])
            x -= 1
            y -= 1
        elif move == UP:
            aligned_seq1.append(seq1[x - 1])
            aligned_seq2.append('-')
            x -= 1
        else:
            aligned_seq1.append('-')
            aligned_seq2.append(seq2[y - 1])
            y -= 1

        move = next_move(score_matrix, x, y)

    aligned_seq1.append(seq1[x - 1])
    aligned_seq2.append(seq1[y - 1])

    return ''.join(reversed(aligned_seq1)), ''.join(reversed(aligned_seq2))

def next_move(score_matrix, x, y):
    diag = score_matrix[x - 1][y - 1]
    up   = score_matrix[x - 1][y]
    left = score_matrix[x][y - 1]
    if diag >= up and diag >= left:     # Tie goes to the DIAG move.
        return 1   # 1 signals a DIAG move. 0 signals the end.
    elif up > diag and up >= left:      # Tie goes to UP move.
        return 2     # UP move or end.
    elif left > diag and left > up:
        return 3   # LEFT move or end.
    else:
        return 0
