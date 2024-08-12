def solution(s):
    num = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
    answer = 0
    i = 1
    
    while s:
        word = s[:i]
        
        if word.isdigit():
            answer = answer * 10 + int(word)
            s = s[i:]
        elif word in num:
            answer = answer * 10 + num[word]
            s = s[i:]
            i = 1
        else:
            i += 1
            
    return answer