def solution(numbers):
    number = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    answer = ""
    i = 3
    
    while numbers:
        word = numbers[:i]
        
        if word in number:
            answer += str(number.index(word))
            numbers = numbers[i:]
            i = 3
        else:
            i += 1
            
    return int(answer)