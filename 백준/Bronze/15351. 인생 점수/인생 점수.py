for _ in range(int(input())):
    s = input().replace(" ", "")
    score = sum(ord(i) - 64 for i in s)
    print("PERFECT LIFE" if score == 100 else score)