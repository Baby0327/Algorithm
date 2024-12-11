"""
후보 추천하기

- now는 [추천 횟수, 등록일, 추천받은 학생 번호] 순의 데이터를 가지고 있음
- target은 현재 사진이 게시된 학생 중 추천수가 가장 적은 학생들을 대상으로 등록일 기준으로 오름차순 정렬함
"""

import sys
input = sys.stdin.readline

n = int(input())
cnt = int(input())
student = list(map(int, input().split()))
photo = []
pick = {}

for i in range(cnt):
    if len(photo) < n:
        if student[i] in photo:
            pick[student[i]][0] += 1
        else:
            pick[student[i]] = [1, i]
            photo.append(student[i])
    else:
        if student[i] in photo:
            pick[student[i]][0] += 1
        else:
            now = sorted([pick[photo[j]] + [photo[j]] for j in range(n)])
            target = sorted(list(filter(lambda x : x[0] == now[0][0], now)), key=lambda x : x[1])
            photo.remove(target[0][2])
            del pick[target[0][2]]
            pick[student[i]] = [1, i]
            photo.append(student[i])

print(*sorted(photo))