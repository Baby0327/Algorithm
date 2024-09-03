"""
일반 화학 실험
"""

temperature = [float(input())]

while True:
    n = float(input())

    if n == 999:
        break

    temperature.append(n)

    print(f"{temperature[-1] - temperature[-2]:.2f}")