def solution(array, commands):
    answer = []
    for i in commands:
        # 자른 배열을 정렬한 후, 원하는 원소에 접근
        answer.append(sorted(array[i[0]-1 : i[1]])[i[2]-1])
    return answer