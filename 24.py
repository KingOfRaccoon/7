with open("24.txt") as file:
    data = file.read()
    counter = 0
    max_counter = 0
    for i in data:
        if i == 'X':
            counter += 1
        else:
            if max_counter < counter:
                max_counter = counter
            counter = 0
    print(max_counter)
    print(len("XXXXXXXXXXXXXXXXXXX"))
