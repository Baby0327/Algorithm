"""
특정 대문자를 소문자로 바꾸기
"""

a = input()
b = input().split()

print("".join([i.lower() if i in b else i for i in a]))