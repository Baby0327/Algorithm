from collections import deque

n, w, L = map(int, input().split())
truck = list(map(int, input().split()))
bridge = deque()

i = 0
time = 0
while i < n:
    if sum(bridge) + truck[i] <= L:
        bridge.appendleft(truck[i])
        i += 1
    else:
        bridge.appendleft(0)
    time += 1
    if len(bridge) >= w:
        bridge.pop()

while sum(bridge) != 0:
    bridge.appendleft(0)
    if len(bridge) > w:
        bridge.pop()
    time += 1

if w == 1:
    print(time + 1)
else:
    print(time)