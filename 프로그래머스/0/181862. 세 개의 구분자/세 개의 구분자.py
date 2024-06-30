def solution(myStr):
    answer = "".join([i if i not in ["a", "b", "c"] else " " for i in myStr]).split()
    return answer or ["EMPTY"]