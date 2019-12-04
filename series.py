def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))


def lucas(n):
    if n == 2:
        return 1
    if n == 1:
        return 2

    return(lucas(n-2) + lucas(n-1))


def sum_func(n, b=0, c=1):
    if n == 2:
        return b
    if n == 1:
        return c

    return sum_func(n-1, b, c) + sum_func(n-2, b, c)


