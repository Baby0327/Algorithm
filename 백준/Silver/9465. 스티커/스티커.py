"""
스티커
"""

t = int(input())

for i in range(t):
    n = int(input())
    dp = []

    for i in range(2):
        dp.append(list(map(int, input().split())))

    if n == 1:
        print(max(dp[0][-1], dp[1][-1]))
    else:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]

        for j in range(2, n):
            # 두 칸 뒤의 두 열 중 max 값을 골라내지 않아도 됨(한 칸 뒤의 값은 두 칸 뒤의 한 열을 무조건 거치기에 이미 비교한 것과 같음)
            dp[0][j] += max(dp[1][j-1], dp[1][j-2])
            dp[1][j] += max(dp[0][j-1], dp[0][j-2])

        print(max(dp[0][-1], dp[1][-1]))