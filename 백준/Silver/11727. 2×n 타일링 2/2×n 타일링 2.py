n = int(input())

tile = [1, 3]

while len(tile) < n:
    tile.append((tile[-2]*2 + tile[-1])%10007)

print(tile[n-1])