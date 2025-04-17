def solution(rsp):
    tip = {"2" : "0", "0" : "5", "5" : "2"}
    return "".join(tip[i] for i in rsp)