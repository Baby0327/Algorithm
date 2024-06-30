import sys
import heapq

N = int(sys.stdin.readline())

heap = []
for i in range(N):
    tmp = int(sys.stdin.readline())
    if tmp == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heap[0])
            heapq.heappop(heap)
    else:
        heapq.heappush(heap, tmp)