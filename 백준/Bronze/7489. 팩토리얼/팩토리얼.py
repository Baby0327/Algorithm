for _ in range(int(input())):
    n = int(input())
    result = 1

    for i in range(1, n + 1):
        result *= i
    
    print(str(result).rstrip("0")[-1])