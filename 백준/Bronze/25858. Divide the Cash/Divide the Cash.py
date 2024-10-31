n, d = map(int, input().split())
s = [int(input()) for _ in range(n)]
print("\n".join(list(map(str, [i * (d//sum(s)) for i in s]))))