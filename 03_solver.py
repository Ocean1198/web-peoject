"""
solver()
주어진 스도쿠 검증하는 함수.
입력: 스도쿠 문제
출력 
└ 해답의 개수(0/1/2), 2는 2개 이상을 의미
└ 난이도(탐색 횟수)
"""

# board: 풀이할 스도쿠
# br, bc: board row, board column
def solver(board, br, bc) : 

    n = br * bc
    sol = 0
    backtrack = 0

    row = [set(board[i]) for i in range(n)]
    col = [set([r[i] for r in board]) for i in range(n)]
    block = [set() for _ in range(n)]
    block_idx = [(r // br) * br + (c // bc)
             for r in range(n)
             for c in range(n)]
    
    empty_cells = []
    for i in range(len(board)) : 
        for j in range(len(board[0])) : 
            if board[i][j] == 0 : 
                empty_cells.append((i,j))
            block[block_idx[i*n+j]].add(board[i][j])

    def dfs(index) : 
        nonlocal sol, backtrack
        backtrack += 1
        if sol >= 2 : 
            return 2
        if index == len(empty_cells) : 
            # # test
            # for i in board : 
            #     print(*i)
            # sol += 1
            return sol
        
        r, c = empty_cells[index]
        b = (r // br) * br + (c // bc)

        # 규칙 검사
        available = list(
            set(range(1, n+1))
            - row[r]
            - col[c]
            - block[b]
        )
        for num in available : 
            board[r][c] = num
            row[r].add(num)
            col[c].add(num)
            block[b].add(num)
            
            # print(index, depth, board)

            dfs(index+1)
            
            board[r][c] = 0
            row[r].remove(num)
            col[c].remove(num)
            block[b].remove(num)

        return sol

    dfs(0)
    return sol, backtrack

# # 직관적으로는 문제가 없지만 해가 존재하지 않는 스도쿠. 정상 작동함(0)
# board = [[1,0,0,0],
#          [0,1,0,0],
#          [0,0,1,0],
#          [0,0,0,0]]

# # sudoku.com의 extreme 난이도 스도쿠. 정상적으로 풀이함(1).
board = [[0,7,0,0,2,0,8,0,0],
         [6,0,0,0,3,0,0,7,0],
         [0,4,8,0,0,0,0,0,0],
         [7,0,0,2,0,0,0,0,9],
         [5,0,0,0,1,0,0,6,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,4,0,0,0,8,0],
         [2,0,0,5,0,0,0,1,0],
         [4,0,5,9,0,0,6,0,0]]

# 해가 여러 개인 스도쿠. 정상적으로 풀이함(2).
# board = [[0,0,0,0],
#          [0,0,0,0],
#          [0,0,0,0],
#          [0,0,0,0]]
solution, backtrack = solver(board, 3, 3)

print(solution, backtrack)


"""
위 알고리즘은 기존 방식에서 해싱을 추가해 시간 복잡도를 줄였지만

1. MRV
2. bitmask

위 2가지로 여전히 성능을 크게 늘릴 수 있다.


또한 위 함수는 난이도 판별을 위해 탐색 횟수를 측정하지만,
각 기술을 구현해 순서대로 풀이하며 특정 기술을 요구하기도 한다.
"""