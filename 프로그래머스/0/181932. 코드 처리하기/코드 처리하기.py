def solution(code):
    answer = ''
    mode = 0
    i = 0
    while i < len(code):
        if code[i] == '1':
            mode = not(mode)
            i += 1
            continue
        if mode:
            if i % 2 == 1:
                answer += code[i]
        else:
            if i % 2 == 0:
                answer += code[i]
        i += 1
    return answer or 'EMPTY'