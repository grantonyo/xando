matrix = [
    ['  ', 'a', 'b', 'c'],
    ['1|', '-', '-', '-'],
    ['2|', '-', '-', '-'],
    ['3|', '-', '-', '-']
]

def display_func(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

player = 1
par = 'x'
end_check=True
def xo_func():
    if par=='x':
        return 'x'
    else:
        return 'o'

def player_change_func():
    global player
    global par
    if player==1 and par=='x':
        player=2
        par='o'
    else:
        player=1
        par='x'
def field_change_func(inp):
    field_names_list=['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    if inp in field_names_list:
        dict = {'a': 1, 'b': 2, 'c': 3}
        input_list = int(inp[1]), dict[inp[0]],
        if matrix[input_list[0]][input_list[1]] == 'x' or matrix[input_list[0]][input_list[1]] == 'o':
            print(f"This square is not empty. Add value to another square.")
            print(f"Player{player}'s turn (add {par}):", end=" ")
            field_change_func(input())
        else:
            matrix[input_list[0]][input_list[1]]=xo_func()
            display_func(matrix)
    else:
        print(f"Incorrect value. Try again. Add parameter from this list: {field_names_list}")
        print(f"Plyaer{player}'s turn (add {par}):", end=" ")
        field_change_func(input())
def completion_check_func (matrix):
    col1, col2, col3 = [], [], [],
    dgnl1, dgnl2 = [], []
    cnt1, cnt2, cnt3 = 0, 3, 0
    global end_check
    for row in matrix:
        if row.count(par) == 3:
            print(f'End of game. Player {player} is a winner.')
            end_check=False
            break
        else:
            col1.append(row[1])
            col2.append(row[2])
            col3.append(row[3])
            dgnl1.append(row[cnt1])
            cnt1 += 1
            dgnl2.append(row[cnt2])
            cnt2 -= 1
            if row.count("-")==0:
                cnt3+=1
    if col1.count(par) == 3 or col2.count(par) == 3 or col3.count(par) == 3:
        print(f"End of game. Player {player} is a winner")
        end_check = False
    elif dgnl1.count(par) == 3 or dgnl2.count(par) == 3:
        print(f"End of game. Player {player} is a winner")
        end_check = False
    elif cnt3==4:
        print(f"End of game. Draw. No winner.")
        end_check = False
    else:
        player_change_func()

display_func(matrix) #command that shows the initial xando filed
while end_check:
    print(f"Plyaer {player}'s turn (add {par}):", end=" ")
    field_change_func(input())
    completion_check_func(matrix)