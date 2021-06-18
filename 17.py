counter = 0
min_num = 0
for i in range(1024, 2048 + 1):
    if i % 7 == 0 and i % 11 != 0 and i % 19 != 0:
        counter += 1
        if min_num == 0:
            min_num = i
print(counter, min_num)