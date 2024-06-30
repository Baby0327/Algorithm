def solution(myString, pat):
    answer = int(pat.upper() in myString.upper())
    return answer