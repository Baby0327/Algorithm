n = int(input())
num = map(int, input().split())
result = sum(num)

if result > 0:
    print("Right")
elif result == 0:
    print("Stay")
else:
    print("Left")