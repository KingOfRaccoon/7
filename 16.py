def f(n):
    if n < 4:
        return n - 1
    elif n > 3:
        return f(n - 2) + g(n - 1)


def g(n):
    if n < 3:
        return n + 1
    elif n > 2:
        return g(n - 2) + f(n - 1)


print(f(25))
