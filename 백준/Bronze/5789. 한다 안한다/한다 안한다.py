"""
한다 안한다
"""

n = int(input())

for i in range(n):
    word = list(map(int, input()))

    if len(word) % 2:
        a, b = word[len(word)//2 - 1], word[len(word)//2 + 1]
    else:
        a, b = word[len(word)//2 - 1], word[len(word)//2]

    print("Do-it" if not a ^ b else "Do-it-Not")