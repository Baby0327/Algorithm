A, B = map(int, input().split())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

union = list(set(A_list) | set(B_list))
intersection = list(set(A_list) & set(B_list))

print(len(union)-len(intersection))