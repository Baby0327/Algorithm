def solution(phone_book):
    
    phoneNum = {}
    for num in phone_book:
        phoneNum[num] = 0
        
    for num in phone_book:
        start = ""
        for i in num:
            start += i
            # 자기 자신이 아닌 접두어로써 존재한다면 False 반환
            if start in phoneNum and start != num:
                return False

    return True