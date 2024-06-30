def solution(todo_list, finished):
    answer = [a for a, b in zip(todo_list, finished) if not b]
    return answer