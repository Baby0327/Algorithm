def solution(my_string, indices):
    my_string = list(my_string)
    for i in indices:
        my_string[i] = ""
    answer = "".join(my_string)
    return answer