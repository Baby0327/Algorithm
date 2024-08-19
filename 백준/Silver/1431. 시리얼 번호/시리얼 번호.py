"""
시리얼 번호
"""

n = int(input())
word = []

for i in range(n):
    word.append(input())

word.sort(key=lambda x : (len(x), sum(int(i) for i in x if i.isdigit()), x))

for i in word:
    print(i)