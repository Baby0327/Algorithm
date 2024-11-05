n = int(input())
print("yummy" if len(set(i for i in input().split() if i.endswith("Cheese"))) >= 4 else "sad")