import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
s = ""
count = 0
i, j = 0, n - 1

for _ in range(n):
    s += input().rstrip()

while i <= j:
    if s[i] < s[j]:
        print(s[i])
        i += 1
    elif s[i] > s[j]:
        print(s[j])
        j -= 1
    else:
        ii, jj = i + 1,  j - 1
        check = True

        while ii <= jj and check:
            if s[ii] < s[jj]:
                print(s[i])
                i += 1
                check = False
            elif s[ii] > s[jj]:
                print(s[j])
                j -= 1
                check = False
                break
            ii += 1
            jj -= 1

        if check:
            print(s[i])
            i += 1

    count += 1

    if count % 80 == 0:
        print("\n")