"""
문자열 폭발

알게 된 점 !!!
    - deque를 사용했을 경우, Line 18에서 TypeError 발생
        -> sequence index must be integer, not 'slice'
    - deque는 slicing을 지원하지 않기 때문
    - list로 바꾸어 slicing해야 함
    - 본 문제는 deque를 사용하지 않아도 충분히 해결할 수 있었음
"""

word = input()
bomb = list(input())
l = len(bomb)
result = []

for i in word:
    result.append(i)
    if len(result) >= l and result[-l:] == bomb:
        for j in range(l):
            result.pop()

print("".join(result) if result else "FRULA")