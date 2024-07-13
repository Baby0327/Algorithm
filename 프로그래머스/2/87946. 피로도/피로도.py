answer = 0


def dfs(k, count):
    global answer   # global은 함수 내에서 전역변수의 값을 변경할 때 선언 필수
    
    if count > answer:
        answer = count

    for i in range(len(dungeon)):
        if k >= dungeon[i][0] and not visited[i]:
            visited[i] = True
            dfs(k - dungeon[i][1], count + 1)
            visited[i] = False


def solution(k, dungeons):
    global dungeon, visited
    
    dungeon = dungeons  # 매개변수로 매번 전달하기 번거로워 전역변수로 선언
    visited = [False] * len(dungeon)
    
    dfs(k, 0)
    
    return answer