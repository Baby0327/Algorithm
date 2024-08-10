def solution(s):
    answer = s.split(" ")
    
    for word in range(len(answer)):
        if answer[word].isalpha():
            answer[word] = answer[word][0].upper() + answer[word][1:].lower()
        else:
            answer[word] = answer[word].lower()
        
    return " ".join(answer)