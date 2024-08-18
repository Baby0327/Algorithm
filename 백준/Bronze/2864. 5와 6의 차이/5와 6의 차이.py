"""
5와 6의 차이
"""

num = input()

mini = num.replace("6", "5")
maxi = num.replace("5", "6")

print(sum(map(int, mini.split())), sum(map(int, maxi.split())))