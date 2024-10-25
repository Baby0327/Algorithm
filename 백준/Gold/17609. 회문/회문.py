import sys
input = sys.stdin.readline
print = sys.stdout.write

for _ in range(int(input())):
    s = input().rstrip()
    i, j = 0, len(s) - 1
    result = 0

    while i <= j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            if i <= j - 1:
                temp = s[:j] + s[j + 1:]
                if temp == temp[::-1]:
                    result = 1
                    break
            if i + 1 < j:
                temp = s[:i] + s[i + 1:]
                if temp == temp[::-1]:
                    result = 1
                    break
            result = 2
            break

    print(f"{result}\n")