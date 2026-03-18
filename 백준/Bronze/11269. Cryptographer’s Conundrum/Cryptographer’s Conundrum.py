s = input()
p = "PER" * (len(s)//3)
print(len([0 for i, j in zip(s, p) if i != j]))