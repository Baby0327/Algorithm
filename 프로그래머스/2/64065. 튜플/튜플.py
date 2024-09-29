def solution(s):
    num = []
    temp = ""
    
    for i in s[1:-1]:
        if i.isdigit():
            temp += i
        elif i == ",":
            num.append(int(temp))
            temp = ""
            
    if temp:
        num.append(int(temp))
        
    return sorted(list(set(num)), key=lambda x : -num.count(x))