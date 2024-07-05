def solution(numbers):
    # str형의 리스트로 변환한 후, x*3(원소가 1000 이하이기 때문) 기준으로 내림차순 정렬
    string = sorted(list(map(str, numbers)), key = lambda x : x*3, reverse = True)
    
    # 0 처리를 위해 str -> int -> str 로 변환 후 반환
    return str(int("".join(string)))