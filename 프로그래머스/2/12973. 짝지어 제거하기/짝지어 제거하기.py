from collections import deque

def solution(s):
    i = 0
    string = deque()
    
    # deque에 순서대로 append하며 마지막 두 원소가 일치할 때 pop
    while i != len(s):
        string.append(s[i])
        if len(string) > 1 and string[-1] == string[-2]:
            string.pop()
            string.pop()
        i += 1
    
    return 0 if string else 1