"""
IT Passport Examination
"""

n = int(input())

for i in range(n):
    num, a, b, c = map(int, input().split())
    result = "PASS" if a >= 35 * 0.3 and b >= 25 * 0.3 and c >= 40 * 0.3 and a + b + c >= 55 else "FAIL"

    print(num, a + b + c, result)