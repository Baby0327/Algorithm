from collections import deque

n, k = map(int, input().split())

person = deque([i+1 for i in range(n)])

print('<',end="")
while len(person) > 1:
    person.rotate(-(k-1))
    print(person.popleft(), end="")
    print(',', end=" ")

print(person.popleft(),end=">")