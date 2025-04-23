def solution(myString, pat):
    return myString[:-myString[::-1].index(pat[::-1])] or myString