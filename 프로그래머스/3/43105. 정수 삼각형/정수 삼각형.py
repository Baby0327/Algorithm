def solution(triangle):
    dp = [[triangle[0][0]]]
    
    for i in range(1, len(triangle)):
        temp = []
        
        # 양 끝은 그대로, 중앙부는 더 큰 값을 선택하여 계산
        for j in range(len(triangle[i])):
            if j == 0:
                temp.append(dp[i-1][j] + triangle[i][j])
            elif j == len(triangle[i]) - 1:
                temp.append(dp[i-1][j-1] + triangle[i][j])
            else:
                temp.append(max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j])
                
        dp.append(temp)
    
    return max(dp[-1])