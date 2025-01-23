cnt = 0

while 1:
    a = input()
    b = input()

    if a == b == "END":
        break

    cnt += 1
    print(f"Case {cnt}: {'same' if sorted(a) == sorted(b) else 'different'}")