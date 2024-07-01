import sys

T = int(sys.stdin.readline())

for i in range(T):
    result = list(sys.stdin.readline().split())
    while True:
        tmp = list(sys.stdin.readline().split())
        if " ".join(tmp) == "what does the fox say?":
            break
        result = [x for x in result if x != tmp[-1]]
    print(" ".join(result))