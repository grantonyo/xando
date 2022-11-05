# 1. Initial xando field:
matrix = [
    ['  ' , 'a', 'b', 'c'],
    ['1|', '-', '-', '-'],
    ['2|', '-', '-', '-'],
    ['3|', '-', '-', '-']
]

# 2. Function that displays matrix:
def display_func(matrix):
    for row in matrix:
        for element in row:
            print(element, end =" ")
        print()
display_func(matrix) #command that shows the initial xando filed

#3. Functions that change xando field:
def player1_turn_func(par):
    dict = {'a': 1, 'b': 2, 'c': 3}
    input_list = int(par[1]), dict[par[0]],
    matrix[input_list[0]][input_list[1]]="x"
    display_func(matrix)

def player2_turn_func(par):
    dict = {'a': 1, 'b': 2, 'c': 3}
    input_list = int(par[1]), dict[par[0]],
    matrix[input_list[0]][input_list[1]]="o"
    display_func(matrix)

#4. Function that checks if the game ended:
def completion_check_func(matrix):
    col1, col2, col3 = [], [], [],
    dgnl1, dgnl2 = [], []
    cnt1, cnt2 = 0, 3
    for row in matrix:
        if row.count('x') == 3:
            print("End of game. Player 1 is a winner")
            break
        else:
            col1.append(row[1])
            col2.append(row[2])
            col3.append(row[3])
            dgnl1.append(row[cnt1])
            cnt1 += 1
            dgnl2.append(row[cnt2])
            cnt2 -= 1
    if col1.count('x') == 3 or col2.count('x') == 3 or col3.count('x') == 3:
        print("End of game. Player 1 is a winner")
    elif dgnl1.count('x') == 3 or dgnl2.count('x') == 3:
        print("End of game. Player 1 is a winner")


