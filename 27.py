def getAll_kr17(data: list):
    all_kr17 = []
    for i in data:
        if i % 17 == 0:
            all_kr17.append(i)
    return all_kr17

def getDataIndex17(data: list, data17: list):
    data_and_index_17 = []
    for i in range(len(data)):
        for j in range(len(data17)):
            if data[i][1] in data17:
                data_and_index_17.append(data[i])
                break
    return data_and_index_17


with open("27-B.txt") as file:
    data = file.read().split()
    for i in range(len(data)):
        data[i] = int(data[i])
    size = data.pop(0)
    print(data)
    data_and_index = [[i, data[i]] for i in range(len(data))]
    data17 = getAll_kr17(data)
    print(data_and_index)
    print(data17)
    data_and_index_17 = (getDataIndex17(data_and_index, data17))
    counter = 0
    sums = []
    for i in data_and_index_17:
        index = i[0]
        num = i[1]
        for j in data_and_index:
            index_j = j[0]
            num_j = j[1]
            if abs(index - index_j) >= 3:
                counter += 1
                sums.append(num_j * num)
    print(len(data_and_index))
    print(len(data_and_index_17))
    print(sums)
    print(counter)