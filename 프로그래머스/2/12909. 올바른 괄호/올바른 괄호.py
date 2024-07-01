def solution(s):
    word = []
    
    for i in s:
        word.append(i)
        # 리스트 끝의 두 원소가 각각 올바른 괄호일 경우, 이를 pop하여 제거
        if len(word) >= 2 and (word[-2] == "(" and word[-1] == ")"):
            word.pop()
            word.pop()
            
    # 남은 괄호가 없을 경우는 True, 아니면 False 반환
    return len(word) == 0