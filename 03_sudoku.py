import random

# br: block row, bc: block column
# cx: current x
# cy: current y
def make(br, bc, cx = 0, cy = 0, board = None, seed = 42) : 

    # n: size of sudoku(n*n size), max number(1~n)
    n = br*bc
    if board == None :
        random.seed(seed)
        board = [[0 for _ in range(n)] for _ in range(n)]

    if cy == n : 
        print(board)
        return True

    available = {i for i in range(1, n + 1)}
    board[cx][cy] = random.choice(list(available))
    if cx == n-1 : 
        if make(br, bc, 0, cy+1, board) :
            return board
    else : 
        if make(br, bc, cx+1, cy, board) :
            return board
    board[cx][cy] = 0

# test code: make 4*4 sudoku
make(2, 2)