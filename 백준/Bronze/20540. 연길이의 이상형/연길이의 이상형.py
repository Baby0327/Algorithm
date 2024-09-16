"""
연길이의 이상형
"""

mbti = {"I" : "E", "E" : "I", "S" : "N", "N" : "S", "T" : "F", "F" : "T", "J" : "P", "P" : "J"}

for i in input():
    print(mbti[i], end="")