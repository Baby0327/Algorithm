def track(a, b, c, p):
    return int(a * (b - p)**c)

def field(a, b, c, p):
    return int(a * (p - b)**c)

for _ in range(int(input())):
    record = list(map(int, input().split()))
    score = (track(9.23076, 26.7, 1.835, record[0]) + field(1.84523, 75, 1.348, record[1])
             + field(56.0211, 1.5, 1.05, record[2]) + track(4.99087, 42.5, 1.81, record[3])
             + field(0.188807, 210, 1.41, record[4]) + field(15.9803, 3.8, 1.04, record[5])
             + track(0.11193, 254, 1.88, record[6]))
    print(score)