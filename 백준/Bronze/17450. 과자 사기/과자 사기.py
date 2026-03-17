p = [list(map(int, input().split())) for _ in range(3)]
p[0] = [(p[0][1] * 10) / (p[0][0] * 10 - int(500 if p[0][0] * 10 >= 5000 else 0)), "S"]
p[1] = [(p[1][1] * 10) / (p[1][0] * 10 - int(500 if p[1][0] * 10 >= 5000 else 0)), "N"]
p[2] = [(p[2][1] * 10) / (p[2][0] * 10 - int(500 if p[2][0] * 10 >= 5000 else 0)), "U"]
p.sort()
print(p[-1][-1])