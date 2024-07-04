def solution(citations):
    # 편의를 위해 내림차순으로 정렬
    count = sorted(citations, reverse=True)
    
    for i in range(len(count)):
        # 인용 횟수가 해당 논문의 인덱스(해당 논문 인용 횟수 이상으로 인용된 논문 수) 이하일 때 break
        if count[i] <= i:
            return i
    
    # 이외의 경우, 배열의 길이 반환 (ex. critations = [20, 10])
    return len(citations)