def solution(sides):
    sides.sort()

    return len([1 for i in range(sides[1] - sides[0] + 1, sides[1])]) + len([1 for i in range(sides[1], sides[0] + sides[1])])