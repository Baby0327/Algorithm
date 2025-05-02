def solution(myString):
    return "".join([i if ord(i) > ord("l") else "l" for i in myString])