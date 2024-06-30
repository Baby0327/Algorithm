x, y, w, s = map(int, input().split())
test = max(x, y)-min(x, y)

if 2*w >= s:
    if test%2 == 0:
        result = min(max(x, y)*s, min(x, y)*s + test*w)
    else:
        result = min(min(x, y)*s + test*w, min(x, y)*s + (test-1)*s + w)
    print(result)
else:
    result = w*(x+y)
    print(result)