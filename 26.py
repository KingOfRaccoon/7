with open("26.txt") as file:
    data = file.read().split()
    for i in range(len(data)):
        data[i] = int(data[i])
    size = data.pop(0)
    size_otl = data.pop(0)
    size_xor = data.pop(0)
    otl = []
    xor = []
    data.sort(reverse=True)
    for i in range(size):
        if 0 <= i < size_otl:
            otl.append(data[i])
        elif size_otl <= i < size_otl + size_xor:
            xor.append(data[i])
    print(size_otl, len(otl))
    print(size_xor, len(xor))
    print(data)
    print(otl)
    print(xor)
    print(sum(otl) / len(otl))
    print(sum(xor) / len(xor))
