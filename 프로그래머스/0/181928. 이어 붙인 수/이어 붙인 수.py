def solution(num_list):
    return int("".join(str(num_list[i]) for i in range(len(num_list)) if num_list[i] % 2)) + int("".join(str(num_list[i]) for i in range(len(num_list)) if num_list[i] % 2 == 0))