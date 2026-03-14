s = input()
n = len(s)
s1 = "." + "".join(".#.." if i % 3 < 2 else ".*.." for i in range(n))
s2 = "." + "".join("#.#." if i % 3 < 2 else "*.*." for i in range(n))
s3 = "#"

for i in range(n):
    if i % 3 < 2:
        s3 += "." + s[i] + ".#"
    else:
        s3 = s3[:-1]
        s3 += "*." + s[i] + ".*"

print(s1)
print(s2)
print(s3)
print(s2)
print(s1)
