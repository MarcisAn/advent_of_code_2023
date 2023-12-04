cards = open("input/day4.txt").read().split("\n")

#part 1
sum = 0
for card in cards:
    wining_nums_str = card.split(": ")[1].split(" | ")[0].split(" ")
    recived_nums_str = card.split(": ")[1].split(" | ")[1].split(" ")
    wining_nums_list = []
    recived_nums_list = []
    for i in wining_nums_str:
        if not i == "":
            wining_nums_list.append(i)
    for i in recived_nums_str:
        if not i == "":
            recived_nums_list.append(i)

    value = 0
    for recived in recived_nums_list:
        if recived in wining_nums_list:
            if value == 0:
                value = 1
            else:
                value *= 2
    sum += value
    print(recived_nums_list)
    print(wining_nums_list)
    print(value)
    print(sum)
