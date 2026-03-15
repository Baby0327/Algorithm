n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
cnt = []

for i in a:
    if cnt:
        check = 1
        for j in range(len(cnt)):
            if i < cnt[j]:
                cnt[j] = i
                check = 0
                break
        if check:
            cnt.append(i)
    else:
        cnt.append(i)

print(len(cnt))