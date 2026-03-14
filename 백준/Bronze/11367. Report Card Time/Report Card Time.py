import sys
input = sys.stdin.readline
print = sys.stdout.write

def score(n):
    if n > 96:
        return "A+"
    elif n > 89:
        return "A"
    elif n > 86:
        return "B+"
    elif n > 79:
        return "B"
    elif n > 76:
        return "C+"
    elif n > 69:
        return "C"
    elif n > 66:
        return "D+"
    elif n > 59:
        return "D"
    else:
        return "F"

for _ in range(int(input())):
    name, num = input().rstrip().split()
    print(name + " " + score(int(num)) + "\n")