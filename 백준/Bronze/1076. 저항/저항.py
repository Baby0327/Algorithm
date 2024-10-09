"""
저항
"""

temp = ""
color = {"black" : 0, "brown" : 1, "red" : 2, "orange" : 3, "yellow" : 4, "green" : 5, "blue" : 6, "violet" : 7, "grey" : 8, "white" : 9}

for i in range(2):
    temp += str(color[input()])

print(int(temp) * (10 ** color[input()]))