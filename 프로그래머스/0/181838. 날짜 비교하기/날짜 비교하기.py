def solution(date1, date2):
    answer = int(int("".join(map(str, date1))) < int("".join(map(str, date2))))
    return answer