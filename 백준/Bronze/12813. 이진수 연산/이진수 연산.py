"""
이진수 연산
"""

a = int(input(), 2)
b = int(input(), 2)
length = 100000
no = 2 ** length - 1

print(bin(a & b)[2:].zfill(length))
print(bin(a | b)[2:].zfill(length))
print(bin(a ^ b)[2:].zfill(length))
print(bin(a ^ no)[2:].zfill(length))
print(bin(b ^ no)[2:].zfill(length))