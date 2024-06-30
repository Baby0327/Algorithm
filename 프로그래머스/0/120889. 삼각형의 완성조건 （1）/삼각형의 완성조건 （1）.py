def solution(sides):
    sides.sort()
    answer = 1 + int(sides[0] + sides[1] <= sides[2])
    return answer