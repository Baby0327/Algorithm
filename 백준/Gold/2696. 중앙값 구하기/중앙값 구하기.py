import heapq
import sys
input = sys.stdin.readline

for i in range(int(input())):
    m = int(input())
    maxi = []
    mini = []
    result = []

    for j in range((m - 1) // 10 + 1):
        num = list(map(int, input().split()))

        for k in range(1, len(num) + 1):
            if k % 2:
                heapq.heappush(maxi, -num[k - 1])
                if mini and -maxi[0] > mini[0]:
                    temp_maxi = heapq.heappop(maxi)
                    temp_mini = heapq.heappop(mini)
                    heapq.heappush(maxi, -temp_mini)
                    heapq.heappush(mini, -temp_maxi)
                result.append(-maxi[0])
            else:
                heapq.heappush(mini, num[k - 1])

    l = len(result)
    print(l)

    if l <= 10:
        print(*result)
    else:
        for i in range(l):
            print(result[i], end=" ")
            if i % 10 == 9:
                print()