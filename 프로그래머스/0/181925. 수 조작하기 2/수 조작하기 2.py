def solution(numLog):
    test = {1:'w', -1:'s', 10:'d', -10:'a'}
    answer = "".join([test[numLog[i] - numLog[i-1]]for i in range(1, len(numLog))])
    return answer