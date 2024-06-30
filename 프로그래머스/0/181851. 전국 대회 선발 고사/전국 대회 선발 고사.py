def solution(rank, attendance):
    three = sorted([rank[i] for i in range(len(rank)) if attendance[i]])[:3]
    answer = 10000 * rank.index(three[0]) + 100 * rank.index(three[1]) + rank.index(three[2])
    return answer