def solution(my_string):
    return sum(map(int, "".join([i if i.isdigit() else " " for i in my_string]).split()))