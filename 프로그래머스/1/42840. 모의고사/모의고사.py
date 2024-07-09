def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = {}
    
    for i in range(len(answers)):
        if answers[i] == p1[i % len(p1)]:
            count[1] = count.get(1, 0) + 1
        if answers[i] == p2[i % len(p2)]:
            count[2] = count.get(2, 0) + 1
        if answers[i] == p3[i % len(p3)]:
            count[3] = count.get(3, 0) + 1
    
    # 맞춘 문제가 많은 순으로, 같으면 오름차순으로 정렬한 후에 최고점인 사람만 반환
    result = sorted(list(count.items()), key=lambda x : (-x[1], x[0]))
    
    return [i for i, j in result if j == result[0][1]]