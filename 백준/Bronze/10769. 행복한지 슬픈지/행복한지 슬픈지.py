m = input()
h = m.count(":-)")
s = m.count(":-(")

if not h + s:
    print("none")
elif h == s:
    print("unsure")
elif h > s:
    print("happy")
else:
    print("sad")