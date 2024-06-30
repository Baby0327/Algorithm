x, y = map(int, input().split())

month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = 0
for i in range(x):
    day += month[i]

day += y

result = day % 7

inging = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

if result == 0:
    print("SUN")
elif result == 1:
    print("MON")
elif result == 2:
    print("TUE")
elif result == 3:
    print("WED")
elif result == 4:
    print("THU")
elif result == 5:
    print("FRI")
elif result == 6:
    print("SAT")