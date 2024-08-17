"""
오타맨 고창영
"""

t = int(input())

for i in range(t):
    index, word = input().split()
    print(word[:int(index)-1] + word[int(index):])