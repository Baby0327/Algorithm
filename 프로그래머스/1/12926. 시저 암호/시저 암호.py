def solution(s, n):
    answer = ""
    
    for i in s:
        if i == " ":
            answer += i
        elif ord(i) >= 97:
            temp = ord(i) + n
            answer += chr(temp) if temp < 97 + 26 else chr(temp - 26)
        else:
            temp = ord(i) + n
            answer += chr(temp) if temp < 65 + 26 else chr(temp - 26)
            
    return answer