s = input()
w = ["asdf", "jkl;"]

if s == "".join(w):
    print("stairs")
elif s == "".join(w)[::-1]:
    print("reverse")
elif s in (w[0][::-1] + w[1], w[1] + w[0][::-1]):
    print("in-out")
elif s in (w[0] + w[1][::-1], w[1][::-1] + w[0]):
    print("out-in")
else:
    print("molu")