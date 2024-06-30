def solution(myString, pat):
    pat = pat.replace('A', 'C').replace('B', 'A').replace('C', 'B')
    answer = int(pat in myString)
    return answer