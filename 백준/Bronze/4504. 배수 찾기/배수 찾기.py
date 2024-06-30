n = int(input())

while True:
    number = int(input())
    if number != 0:
        if number % n == 0:
            print(f"{number} is a multiple of {n}.")
        else:
            print(f"{number} is NOT a multiple of {n}.")
    else:
        break