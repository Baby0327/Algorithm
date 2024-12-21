card = {}

for _ in range(int(input())):
    name, cnt = input().split()
    card[name] = card.get(name, 0) + int(cnt)

print("YES" if 5 in card.values() else "NO")