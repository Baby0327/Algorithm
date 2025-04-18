def solution(numbers):
    english = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9, "ten" : 10}
    answer = []
    i = 3
    
    while numbers:
        now = numbers[:i]
        
        if now in english:
            answer.append(english[now])
            numbers = numbers[i:]
            i = 3
        else:
            i += 1
    
    
    return int("".join(map(str, answer)))