def solution(rsp):
    tmp = ["5", "0", "2"]
    answer = "".join(tmp[tmp.index(i) - 1] for i in rsp)
    return answer