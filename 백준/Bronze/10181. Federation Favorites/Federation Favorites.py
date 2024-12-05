while 1:
    n = int(input())

    if n == -1:
        break

    num = [i for i in range(1, n) if n % i == 0]

    if sum(num) == n:
        print(n, "=", " + ".join(map(str, num)))
    else:
        print(n, "is NOT perfect.")