# Board
matrix = [
    ['  ', 'a', 'b', 'c'],
    ['1|', '-', '-', '-'],
    ['2|', '-', '-', '-'],
    ['3|', '-', '-', '-']
]


# Function that displays board in terminal
def display_func(mat):
    for row in mat:
        for element in row:
            print(element, end=" ")
        print()


player = 1  # var with player number (player 1 begins the game)
par = 'x'  # var with 'x' or 'o' values (player 1 begins with 'x' in it's first turn
end_check = True  # checks if the game ended ("False" value is assigned when board has no more empty fields)


# Function that changes par value from 'x' to 'o' and from 'o' to 'x' in each next turn
def xo_change_func():
    if par == 'x':
        return 'x'
    else:
        return 'o'


# Function that changes player number in each next turn
def player_change_func():
    global player
    global par
    if player == 1 and par == 'x':
        player = 2
        par = 'o'
    else:
        player = 1
        par = 'x'


# Function that adds 'x' and 'o' to the board upon the end of each turn with parameter check
# (correctness of values added by the player) and cell status check (empty or not empty)
def board_change_func(inp):
    field_names_list = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    if inp in field_names_list:
        valdict = {'a': 1, 'b': 2, 'c': 3}
        input_list = int(inp[1]), valdict[inp[0]],
        if matrix[input_list[0]][input_list[1]] == 'x' or matrix[input_list[0]][input_list[1]] == 'o':
            print(f"This square is not empty. Add value to another square.")
            print(f"Player {player}'s turn (add {par}):", end=" ")
            board_change_func(input())
        else:
            matrix[input_list[0]][input_list[1]] = xo_change_func()  # adds 'x' or 'o' to the board
            display_func(matrix)
    else:
        print(f"Incorrect value. Try again. Add parameter from this list: {field_names_list}")
        print(f"Player {player}'s turn (add {par}):", end=" ")
        board_change_func(input())


# Function that checks and identifies end of the game
def completion_check_func(mat):
    col1, col2, col3 = [], [], []  # vars needed to check three 'x's or 'o's in columns
    dgnl1, dgnl2 = [], []  # var needed to check three 'x's or 'o's in diagonals
    cnt1, cnt2, cnt3 = 0, 3, 0  # support vars
    global end_check
    for row in mat:
        if row.count(par) == 3:
            print(f'End of game. Player {player} is a winner.')
            end_check = False
            break
        else:
            col1.append(row[1])
            col2.append(row[2])
            col3.append(row[3])
            dgnl1.append(row[cnt1])
            cnt1 += 1
            if row[0] != "  ":
                dgnl2.append(row[cnt2])
                cnt2 -= 1
            if row.count("-") == 0:
                cnt3 += 1
    if col1.count(par) == 3 or col2.count(par) == 3 or col3.count(par) == 3:
        print(f"End of game. Player {player} is a winner")
        end_check = False
    elif dgnl1.count(par) == 3 or dgnl2.count(par) == 3:
        print(f"End of game. Player {player} is a winner")
        end_check = False
    elif cnt3 == 4:
        print(f"End of game. Draw. No winner.")
        end_check = False
    else:
        player_change_func()


# game engine as such is in 5 lines below:
display_func(matrix)  # command that shows the initial board
while end_check:
    print(f"Player {player}'s turn (add {par}):", end=" ")  # info about the current turn
    board_change_func(input())  # takes input from player and updates the board accordingly
    completion_check_func(matrix)  # checks game status and stops the game when ended
