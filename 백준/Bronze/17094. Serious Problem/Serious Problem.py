input()
s = input()
count_e = s.count("e")
count_2 = s.count("2")

if count_e > count_2:
    print("e")
elif count_e < count_2:
    print("2")
else:
    print("yee")