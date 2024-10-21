"""
Football Team
"""

dic = {"i" : "e", "e" : "i", "I" : "E", "E" : "I"}

while True:
        try:
            name = input()
            temp = ""
            for i in name:
                if i in dic:
                    temp += dic[i]
                else:
                    temp += i
            print(temp)
        except EOFError:
            break