"""
첫 글자를 대문자로
"""

n = int(input())

for i in range(n):
    line = input()
    
    print(line[0].upper() + line[1:])