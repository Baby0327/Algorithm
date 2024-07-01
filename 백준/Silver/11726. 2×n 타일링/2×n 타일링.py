n = int(input())

tile = [1, 2]

while len(tile) < n:
    tile.append((tile[-1] + tile[-2])%10007)

print(tile[n-1])