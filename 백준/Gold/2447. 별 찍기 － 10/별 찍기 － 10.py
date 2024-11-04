def star(p, now):
    if p == n:
        return now

    temp = []

    for i in range(p):
        temp.append(now[i] * 3)

    for i in range(p):
        temp.append(now[i] + ' ' * p + now[i])

    for i in range(p):
        temp.append(now[i] * 3)

    return star(p * 3, temp)

start = ["***", "* *", "***"]
n = int(input())
print("\n".join(star(3, start)))