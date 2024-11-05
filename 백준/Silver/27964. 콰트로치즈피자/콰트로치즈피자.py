n = int(input())
tp = set()

for i in input().split():
    if i.endswith("Cheese"):
        tp.add(i)

print("yummy" if len(tp) >= 4 else "sad")