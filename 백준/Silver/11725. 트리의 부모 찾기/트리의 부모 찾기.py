import sys
sys.setrecursionlimit(1000000)


def dfs(start):
    for i in graph[start]:
        if not visited[i]:
            visited[i] = start
            dfs(i)


n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

for i in range(2, len(visited)):
    sys.stdout.write(str(visited[i])+"\n")