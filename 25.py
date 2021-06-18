from math import isqrt

def getDels(num: int):
    dels = []
    for i in range(2, isqrt(num)+1):
        if num % i == 0:
            dels.append(i)
    obr_dels = [num//x for x in dels]
    for i in obr_dels: dels.append(i)
    return sorted(list(set(dels)))

counter = 0
for i in range(19960, 20000 + 1):
    dels = getDels(i)
    if len(dels) == 2:
        print(dels, i)
        counter += 1
print(counter)