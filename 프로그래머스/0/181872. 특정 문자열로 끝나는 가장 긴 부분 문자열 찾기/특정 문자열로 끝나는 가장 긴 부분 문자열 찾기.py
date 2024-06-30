def solution(myString, pat):
    answer = myString[:len(myString) - myString[::-1].index(pat[::-1])]
    return answer