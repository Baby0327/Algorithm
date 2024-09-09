"""
인사성 밝은 곰곰이
"""

n = int(input())
emoticon = set()
result = 0

for i in range(n):
    s = input()

    if s == "ENTER":
        result += len(emoticon)
        emoticon.clear()
    else:
        emoticon.add(s)

result += len(emoticon)

print(result)