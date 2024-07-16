def solution(n, words):

    speaking = [words[0]]
    
    for i in range(1, len(words)):
        # 이미 말했던 단어이거나, 끝말을 잇지 않은 말일 때 탈락자 발생
        if (words[i] in speaking) or (words[i][0] != speaking[-1][-1]):
            return [len(speaking) % n + 1, len(speaking) // n + 1]
        else:
            speaking.append(words[i])

    return [0, 0]