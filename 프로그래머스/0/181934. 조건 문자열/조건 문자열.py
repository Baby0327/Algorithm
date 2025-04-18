def solution(ineq, eq, n, m):
    if ineq == "<":
        if (eq == "=" and n <= m) or (eq == "!" and n < m):
            return 1
        else:
            return 0
    else:
        if (eq == "=" and n >= m) or (eq == "!" and n > m):
            return 1
        else:
            return 0