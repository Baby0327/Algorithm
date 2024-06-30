def solution(myString):
    answer = ''.join([i if ord(i) > ord('l') else 'l' for i in myString])
    return answer