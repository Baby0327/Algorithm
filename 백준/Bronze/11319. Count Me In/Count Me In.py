for _ in range(int(input())):
    s = input().lower().replace(" ", "")
    result = len([1 for i in s if i in "aeiou"])
    print(len(s) - result, result)