n = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for _ in range(int(input())):
    x, y = map(int, input().split())
    print(f"{'Yes' if x < 24 and y < 60 else 'No'} {'Yes' if 0 < x < 13 and 0 < y <= n[x] else 'No'}")