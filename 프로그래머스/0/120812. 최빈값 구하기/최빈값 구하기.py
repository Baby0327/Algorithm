def solution(array):
    cnt = sorted([[array.count(i), i] for i in set(array)], reverse = True)
    return -1 if len(cnt) > 1 and cnt[0][0] == cnt[1][0] else cnt[0][1]