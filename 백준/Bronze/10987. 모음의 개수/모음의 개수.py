"""
모음의 개수
"""

vowel = {"a" : 1, "e" : 1, "i" : 1, "o" : 1, "u" : 1}
result = 0
word = input()

for i in word:
    result += vowel.get(i, 0)

print(result)