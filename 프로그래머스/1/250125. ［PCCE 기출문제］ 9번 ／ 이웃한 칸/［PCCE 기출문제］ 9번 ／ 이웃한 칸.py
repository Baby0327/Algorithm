def solution(board, h, w):
    answer = 0
    dr = [-1, 0, 0, 1]
    dc = [0, -1, 1, 0]
    l = len(board)
    
    for i in range(4):
        r = h + dr[i]
        c = w + dc[i]
        
        if (0 <= r < l) and (0 <= c < l) and board[h][w] == board[r][c]:
            answer += 1
            
    return answer