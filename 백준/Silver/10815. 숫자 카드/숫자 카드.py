N = int(input())
card = list(map(int, input().split()))
M = int(input())
test = list(map(int, input().split()))

card = set(card)

for i in test:
    if i in card:
        print(1, end=" ")
    else:
        print(0, end=" ")