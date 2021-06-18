for d in range(1, 1001):
    cope = d
    n = 5
    s = 83
    while s <= 1200:
        s = s + d
        n = n + 6
    if n == 89:
        print(cope)