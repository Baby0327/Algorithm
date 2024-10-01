"""
제곱근
"""

n = int(input())
start = 1
end = 10 ** 400

while start <= end:
    mid = (start + end) // 2
    temp = mid ** 2

    if n == temp:
        print(mid)
        break
    elif n > temp:
        start = mid + 1
    else:
        end = mid - 1