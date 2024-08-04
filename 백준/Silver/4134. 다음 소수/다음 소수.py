"""
다음 소수
"""

import sys

def check(n):
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True


t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())

    # 0과 1의 경우, 소수가 아니기 때문에 결과값이 2임을 따로 처리
    if n in [0,1]:
        sys.stdout.write("2\n")
    else:
        while True:
            if check(n):
                sys.stdout.write(str(n) + "\n")
                break
            else:
                n += 1