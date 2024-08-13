"""
잃어버린 괄호
"""

s = input().split("-")
calc = []

for i in s:
    #eval 사용 시 0으로 시작하는 정수에 관한 오류가 발생하기에, int로 0 처리 후 계산
    temp = i.split("+")
    calc.append(sum([int(num) for num in temp]))

result = calc[0]

for i in range(1, len(calc)):
    result -= calc[i]

print(result)