def solution(balls, share):
    temp1 = 1
    temp2 = 1
    
    for i in range(share):
        temp1 *= balls - i
    
    for i in range(share):
        temp2 *= share - i
        
    return temp1 // temp2