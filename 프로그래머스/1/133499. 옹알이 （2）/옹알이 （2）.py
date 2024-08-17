def solution(babbling):
    answer = 0
    possible = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        i = 1
        before = ""     # 같은 발음이 연속되는지 판단하기 위한 변수 선언
        
        while i <= len(word):
            # 가능한 발음이며 연속되지 않은 발음일 때, 발음할 수 있다고 판단
            if word[:i] in possible and word[:i] != before:
                before = word[:i]
                word = word[i:]
                i = 1
            else:
                i += 1
                
        if len(word) == 0:
            answer += 1
        
    return answer