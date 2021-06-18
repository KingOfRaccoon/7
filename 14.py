num = 4**14 + 64**16 - 81
string = ""
while num > 0:
    string += str(num % 4)
    num = num // 4
print(string)
print(string.count('3'))