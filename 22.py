for x in range(1, 1010):
    cope = x
    a, b = 0, 1
    while x > 0:
        a = a + 1
        b = b * (x % 9)
        x = x // 9
    if a == 3 and b == 18:
        print(cope)