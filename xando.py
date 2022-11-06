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

#3. Parameters  and function that changes player'sturn:
player=1
par='x'
def xo_func():
    if par=='x':
        return 'x'
    else:
        return 'o'

def player_turn_func(inp):
    dict = {'a': 1, 'b': 2, 'c': 3}
    input_list = int(inp[1]), dict[inp[0]],
    matrix[input_list[0]][input_list[1]]=xo_func()
    display_func(matrix)

#4. Function that checks if the game ended:
def completion_check_func(matrix):
    col1, col2, col3 = [], [], [],
    dgnl1, dgnl2 = [], []
    cnt1, cnt2, cnt3 = 0, 3, 0
    for row in matrix:
        if row.count(par) == 3:
            print(f'End of game. Player {player} is a winner')
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
    elif dgnl1.count(par) == 3 or dgnl2.count(par) == 3:
        print(f"End of game. Player {player} is a winner")
    elif cnt3==4:
        print(f"End of game. Draw. No winner.")
    else:
        cnt3=0

#5. Game engine


