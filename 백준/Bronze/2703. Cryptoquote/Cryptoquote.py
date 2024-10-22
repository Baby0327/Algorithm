import sys
input = sys.stdin.readline

for i in range(int(input())):
    enc = input().strip()
    alpha = input().strip()
    
    for j in enc:
        if j.isalpha():
            sys.stdout.write(alpha[ord(j) - 65])
        else:
            sys.stdout.write(j)

    sys.stdout.write("\n")