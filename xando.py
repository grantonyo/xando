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
