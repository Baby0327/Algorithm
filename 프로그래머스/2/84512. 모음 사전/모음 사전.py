# 완전탐색을 통해 모든 경우의 수 구하기
def dfs(l):
    if len(case) == l:
        result.append("".join(case))
        return
        
    for i in range(1, 6):
            case.append(vowel[i-1])
            dfs(l)
            case.pop()
    

def solution(word):
    global result, case, vowel
    
    result = []
    case = []
    vowel = ["A", "E", "I", "O", "U"]
    
    # 길이별 모든 단어 탐색
    for i in range(1, 6):
        dfs(i)
    
    # 사전순으로 정렬한 후, 원소의 인덱스 찾아 반환
    return sorted(result).index(word) + 1