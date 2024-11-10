import sys
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    ab = list(map(int, input().split()))
    result = []

    for j in range(int(input())):
        p = int(input())
        cnt = 0

        for k in range(0, len(ab), 2):
            if ab[k] <= p <= ab[k + 1]:
                cnt += 1
        result.append(cnt)
    print(f"Case #{i + 1}: " + " ".join(map(str, result)))
    input()