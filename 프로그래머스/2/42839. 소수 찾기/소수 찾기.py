"""
알게 된 점 !!!
    - set과 같은 mutable 객체는 함수 내에서 global 선언 없이도 수정이 가능함
        -> mutable 객체는 그 자체가 아니라 객체에 대한 참조를 전달하기 때문
        -> 다만, '수정'이 아닌 '재할당'의 경우는 global 선언 필요
    - immutable 객체 (예: int, str, tuple 등)는 값 수정 시 global 선언 필수임
"""


# 에라토스테네스의 체를 활용하여 범위 내의 소수 구하기
def prime(n):
    global num
    
    num = [True] * (10**n + 1)
    num[0], num[1] = False, False
    
    for i in range(2, int(len(num)**0.5) + 1):
        if num[i]:
            for j in range(i**2, 10**n + 1, i):
                num[j] = False


# numbers로부터 만들 수 있는 길이가 n인 조합 찾기 
def case(n, numbers):
    if len(test) == n:
        result = int("".join(test))
        if num[result]:     # 완성된 값이 소수일 때에만 count에 저장
            count.add(result)
        return
    
    for i in range(len(numbers)):
        if not visited[i]:
            visited[i] = True
            test.append(numbers[i])
            case(n, numbers)
            visited[i] = False
            test.pop()
    
    
def solution(numbers):
    global visited, test, count
    
    count = set()   # 전체 조합 저장 (중복 방지를 위해 set으로 설정)
    n = len(numbers)
    prime(n)
    visited = [False] * n
    test = []
    
    for i in range(1, n+1):
        case(i, numbers)
    
    return len(count)
