import random

# br: block row, bc: block column
# cx: current x
# cy: current y
def make(br, bc, r = 0, c = 0, board = None, seed = 42,
         row = None, col = None, block = None) : 

    # n: size of sudoku(n*n size), max number(1~n)
    n = br * bc
    if board is None : 
        random.seed(seed)
        board = [[0 for _ in range(n)] for _ in range(n)]
        row = [set() for _ in range(n)]
        col = [set() for _ in range(n)]
        block = [set() for _ in range(n)]

    if c == n : 
        return board
    
    block_idx = (r // br) * (n // bc) + (c // bc)

    available = list(
        set(range(1, n+1))
        - row[r]
        - col[c]
        - block[block_idx]
    )

    if not available : 
        return False
    
    random.shuffle(available)
    
    for num in available : 
        board[r][c] = num
        row[r].add(num)
        col[c].add(num)
        block[block_idx].add(num)

        if r == n-1 : 
            result = make(br, bc, 0, c+1, board, seed,
                          row, col, block)
        else : 
            result = make(br, bc, r+1, c, board, seed,
                          row, col, block)
        if result : 
            return result
        
        board[r][c] = 0
        row[r].remove(num)
        col[c].remove(num)
        block[block_idx].remove(num)
        

    return False

# test code: make 4*4 sudoku
board = make(2, 3)
for i in board : 
    print(*i)