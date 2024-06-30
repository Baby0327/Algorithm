N = int(input())

person = list(map(int, input().split()))

count = set(person)

print(len(person)-len(count))