inp = open("./input/day3.txt", "r").read()

valid_number_cords = []

rows = inp.split("\n")

numbers = []

row_index = 0
number= ""

def is_cord_valid(x,y):
    print(x,y)
    #print(inp.split("\n"),x,y)
    #print(x,y)
    #print(inp.split("\n")[y - 1])
    if y != 0:
        top_right = inp.split("\n")[y - 1][x - 1]
        if (top_right != "." and not top_right.isdigit()):
            return True
        if x != 0:
            top_left = inp.split("\n")[y - 1][x+1]
            if (top_left != "." and not top_right.isdigit()):
                return True
        top = inp.split("\n")[y - 1][x]
        if (top != "." and not top.isdigit()):
            return True
    if x != 0:
        left = inp.split("\n")[y][x-1]
        if (left != "." and not left.isdigit()):
            return True
    if x != 139:
        right = inp.split("\n")[y][x+1]
        if (right != "." and not right.isdigit()):
            return True
    if y != 139:
        bot_right = inp.split("\n")[y + 1][x - 1]
        if (bot_right != "." and not bot_right.isdigit()):
            return True
        if x != 0:
            bot_left = inp.split("\n")[y + 1][x+1]
            if (bot_left != "." and not bot_left.isdigit()):
                return True
        bot = inp.split("\n")[y + 1][x + 1]
        if (bot != "." and not bot.isdigit()):
            return True
    return False

def is_number_valid(number):
    x = number[0]
    y = number[1]
    for i in range(0, len(str(number[2]))):
        if is_cord_valid(x+i, y):
            return True

for row in rows:
    tmp_number = ""
    is_previous_digit = False
    starting_cords = []
    symbol_index = 0
    for symbol in row:
        if symbol.isdigit():
            tmp_number += symbol
            if not is_previous_digit:
                starting_cords = [symbol_index, row_index]
            is_previous_digit = True
        else:
            if is_previous_digit or symbol == "\n":
                numbers.append([starting_cords[0], starting_cords[1], int(tmp_number)])
                tmp_number = ""
                is_previous_digit = False
        symbol_index += 1
    row_index += 1

sum = 0

for number in numbers:
    print(number)
    if is_number_valid(number):
        print("true")
        sum += int(number[2])

print(sum)
print(531561)