def solution(arr):
    answer = 0
    before = arr[:]
    while True:
        now = []
        for i in before:
            if i >= 50 and i % 2 == 0:
                now.append(i//2)
            elif i < 50 and i % 2 == 1:
                now.append(i*2+1)
            else:
                now.append(i)
        if before == now:
            break
        answer += 1
        before = now
    return answer