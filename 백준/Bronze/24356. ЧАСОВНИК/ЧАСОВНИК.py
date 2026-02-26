n = list(map(int, input().split()))
s = n[0] * 60 + n[1]
e = n[2] * 60 + n[3] + int(n[:2] > n[2:]) * 60 * 24
print(e - s, (e - s) // 30)