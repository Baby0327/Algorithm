def solution(sequence, k):
    s = e = 0
    answer = [0, len(sequence)]
    now = sequence[0]

    while True:
        if now < k:
            e += 1
            if e == len(sequence): break
            now += sequence[e]
        else:
            if now == k and e - s < answer[1] - answer[0]:
                answer = [s, e]
            now -= sequence[s]
            s += 1
            
    return answer