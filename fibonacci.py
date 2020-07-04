def fibonacci_recursive(n:int) -> int:
    if n < 0:
        print(f"{n} is not a valid input.")

    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_iterative(n:int) -> int:
    if n < 0:
        print(f"{n} is not a valid input.")

    f = [0, 1]

    for i in range(2,n+2):
        f.append(f[i-1] + f[i-2])

    return f[n]


#print(fibonacci_recursive(9))

#print(fibonacci_iterative(9))
