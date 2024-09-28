"""
천재 수학자 성필
"""

from collections import deque

s = input()
process = deque()

for i in s:
    if i in "+-*/":
        b = str(process.pop())
        a = str(process.pop())
        if i == "/":
            i += "/"    # 모든 결과값은 정수이기에 / 가 아닌 //로 변환
        process.append(eval(a + i + b))     # eval은 보안에 취약하기에 권장하지 않음
    else:
        process.append(i)

print(process[0])