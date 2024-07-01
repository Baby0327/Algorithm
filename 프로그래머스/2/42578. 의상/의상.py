def solution(clothes):
    # 종류별 의상 수 저장
    types = {}
    for x, y in clothes:
        types[y] = types.get(y, 0) + 1
    
    # 특정 종류의 의상을 착용하지 않는 경우를 고려하여 +1한 값으로 곱하여 계산
    values = list(types.values())
    answer = 1
    for i in values:
        answer *= (i+1)
        
    # 모든 종류의 의상을 착용하지 않은 경우를 제외하여 반환
    return answer  - 1