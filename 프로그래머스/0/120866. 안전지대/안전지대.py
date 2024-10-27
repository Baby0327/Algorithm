def solution(board):
    n = len(board)
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for k in range(8):
                    r = i + dr[k]
                    c = j + dc[k]
                    if 0 <= r < n and 0 <= c < n and board[r][c] != 1:
                       board[r][c] = 2
            
    return sum(board[i].count(0) for i in range(n))