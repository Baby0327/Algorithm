import heapq
import sys
input = sys.stdin.readline

maxi = []
mini = []

for i in range(1, int(input()) + 1):
    n = int(input())

    if i % 2:
        heapq.heappush(maxi, -n)
    else:
        heapq.heappush(mini, n)

    if mini and -maxi[0] > mini[0]:
        temp_maxi = heapq.heappop(maxi)
        temp_mini = heapq.heappop(mini)
        heapq.heappush(mini, -temp_maxi)
        heapq.heappush(maxi, -temp_mini)

    print(-maxi[0])