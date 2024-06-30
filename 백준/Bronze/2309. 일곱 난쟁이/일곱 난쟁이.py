h = []
for i in range(9):
    h.append(int(input()))

result = []
for i in range(len(h)):
    for j in range(i+1, len(h)):
        if sum(h) - h[i] - h[j] == 100:
            result.append(h[i])
            result.append(h[j])
            break

h.remove(result[0])
h.remove(result[1])
h.sort()
for i in h:
    print(i)