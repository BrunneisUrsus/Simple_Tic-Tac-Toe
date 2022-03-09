win_x = 0
win_o = 0
turn = 1

diagonal = []
anti_diagonal = []

first_line = []
second_line = []
third_line = []

first_column = []
second_column = []
third_column = []

x_value = ["X", "X", "X"]
o_value = ["O", "O", "O"]

value = [" " for i in range(10)]

for i in range(0, 3):
    first_line.append(value[i])
for i in range(3, 6):
    second_line.append(value[i])
for i in range(6, 9):
    third_line.append(value[i])

line = [first_line, second_line, third_line]


def grid(cell):
    print("---------")
    print("|", cell[0][0], cell[0][1], cell[0][2], "|", sep=" ")
    print("|", cell[1][0], cell[1][1], cell[1][2], "|", sep=" ")
    print("|", cell[2][0], cell[2][1], cell[2][2], "|", sep=" ")
    print("---------")


for i in range(3):
    first_column.append(line[i][0])
    second_column.append(line[i][1])
    third_column.append(line[i][2])
    diagonal.append(line[i][i])
    anti_diagonal.append((line[i][-i - 1]))

column = [first_column, second_column, third_column]

while True:
    grid(line)
    move = input("Enter the coordinates: ").split()
    if (len(move[0]) or len(move[1])) > 1 or len(move) != 2:
        print("You should enter numbers!")
    else:
        x_axis = int(move[0]) - 1
        y_axis = int(move[1]) - 1
        if x_axis > 2 or y_axis > 2:
            print("Coordinates should be from 1 to 3!")
            continue
        if line[x_axis][y_axis] == "X" or line[x_axis][y_axis] == "O":
            print("This cell is occupied! Choose another one!")
        else:
            turn += 1
            if turn % 2 == 0:
                line[x_axis][y_axis] = "X"
                column[y_axis][x_axis] = "X"
                if x_axis == y_axis:
                    diagonal[x_axis] = "X"
                    if x_axis == 1:
                        anti_diagonal[x_axis] = "X"
                if abs(x_axis - y_axis) == 2:
                    anti_diagonal[x_axis] = "X"
                grid(line)
            elif turn % 2 != 0:
                line[x_axis][y_axis] = "O"
                column[y_axis][x_axis] = "O"
                if x_axis == y_axis:
                    diagonal[x_axis] = "O"
                    if x_axis == 1:
                        anti_diagonal[x_axis] = "O"
                if abs(x_axis - y_axis) == 2:
                    anti_diagonal[x_axis] = "O"
                grid(line)
        if x_value in line or x_value in column:
            win_x += 1
            break
        elif o_value in line or o_value in column:
            win_o += 1
            break
        if x_value == diagonal or x_value == anti_diagonal:
            win_x += 1
            break
        elif o_value == diagonal or o_value == anti_diagonal:
            win_o += 1
            break
        if turn == 10:
            break
if win_x > 0:
    print("X wins")
elif win_o > 0:
    print("O wins")
else:
    print("Draw")
