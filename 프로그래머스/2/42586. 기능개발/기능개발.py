def solution(progresses, speeds):
    # 기능별 작업일수 계산하여 저장
    work = []
    for p, s in zip(progresses, speeds):
        if (100 - p) % s == 0:
            work.append((100 - p) // s)
        else:
            work.append((100 - p) // s + 1)
    
    max = work[0]
    result = [0]
    for i in work:
        # i 작업일수가 현재 작업일수보다 적게 소요될 경우, 바로 배포
        if i <= max:
            result[-1] += 1
        # i 작업일수가 현재 작업일수보다 더 많이 소요될 경우, i 작업이 끝나는 날에 배포
        else:
            result.append(1)
            max = i
            
    return result