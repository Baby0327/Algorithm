def solution(ineq, eq, n, m):
    answer = int(eval(str(n) + ineq + eq + str(m)) if eq == '=' else eval(str(n) + ineq + str(m)))
    return answer