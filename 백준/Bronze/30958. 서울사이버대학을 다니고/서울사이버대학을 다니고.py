"""
서울사이버대학을 다니고
"""

n = int(input())
word = input()
result = 0

for i in range(26):
    result = max(result, word.count(chr(i+97)))

print(result)