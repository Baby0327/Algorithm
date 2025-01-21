for _ in range(int(input())):
    a, b = input().split()
    print(f"{a} & {b} are {'' if sorted(a) == sorted(b) else 'NOT '}anagrams.")