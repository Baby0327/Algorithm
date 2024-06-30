def solution(id_pw, db):
    answer = "fail"
    for id, pw in db:
        if id_pw[0] == id:
            answer = "wrong pw"
            if id_pw[1] == pw:
                answer = "login"
                break
    return answer