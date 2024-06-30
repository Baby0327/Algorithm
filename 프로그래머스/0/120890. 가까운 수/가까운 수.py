def solution(array, n):
    array.append(n)
    array.sort()
    answer = sorted([array[array.index(n)-1], array[(array.index(n) + 1)%len(array)]], key=lambda x:abs(x-n))
    return answer[0]