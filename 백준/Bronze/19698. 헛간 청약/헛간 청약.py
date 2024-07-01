n, w, h, l = map(int, input().split())
result = (w//l)*(h//l)
if result > n:
    result = n
print(result)