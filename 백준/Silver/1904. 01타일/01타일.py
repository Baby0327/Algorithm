n = int(input())
tile = [1, 2]

while len(tile) < n:
    tile.append((tile[-2] + tile[-1])%15746)

print(tile[n-1])