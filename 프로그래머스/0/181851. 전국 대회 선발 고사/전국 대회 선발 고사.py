def solution(rank, attendance):
    a, b, c = [i[1] for i in (sorted([[value, index] for index, value in enumerate(rank) if attendance[index]])[:3])]
    return 10000 * a + 100 * b + c