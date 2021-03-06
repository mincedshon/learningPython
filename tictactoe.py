m_repeat = True
changeName = True
name_list = []
assign = {}
grid = []
turn = 0
for i in range(9):
    grid.append(" ")

#Getting player's names
def get_names():
    x = 1
    repeat = True

    while repeat:
        name = input(f"Please enter player {x}'s name (max 10 letters): \n")
        print("\n"*50)
        if len(name) > 11:
            print("Your name is too long!")
        if len(name) == 0:
            print("Your name can't be blank!")
        else:
            name_list.append(name)
            if len(name_list) == 2:
                repeat = False
                pass
            x += 1

#Finding who starts first
def start_order():
    global turn
    repeat = True
    answer = ["Y","y","N","n"]

    while repeat:
        start = input(f"Would you like to start first, {name_list[0]}? (Y/N): \n")
        print("\n"*50)
        if start not in answer:
            print("Sorry, I do not understand you.")
        else:
            if start == "Y" or start == "y":
                turn = 1
                break
            else:
                turn = 0
                break

#Assigning X/O to player
def symbol_choice():
    repeat = True
    answer = ["X","x","O","o"]

    while repeat:
        start = input(f"Choose your symbol, {name_list[0]}. (X/O): \n")
        print("\n"*50)
        if start not in answer:
            print("Sorry, I do not understand you.")
        else:
            if start == "X" or start == "x":
                #assign X to namelist[0], O to namelist[1]
                symbol = ["X","O"]
                repeat = False

            else:
                #assign O to namelist[0], X to namelist[1]
                symbol = ["O","X"]
                repeat = False
    global assign
    assign = dict(zip(name_list,symbol))

#Tic tac toe display grid
def show_grid():
    print(" "+f"{grid[6]}"+" | "+f"{grid[7]}"+" | "+f"{grid[8]}")
    print("-"*11)
    print(" "+f"{grid[3]}"+" | "+f"{grid[4]}"+" | "+f"{grid[5]}")
    print("-"*11)
    print(" "+f"{grid[0]}"+" | "+f"{grid[1]}"+" | "+f"{grid[2]}")

def replace():
    repeat = True

    while repeat:
        show_grid()
        #Choose respective symbol from dictionary
        x = input(f"{name_list[turn]}'s turn. Place your {assign[name_list[turn]]}. (1-9): \n")
        print("\n"*50)
        if x.isdigit() == False:
            print("Please enter numbers!")
            continue
        if 1 <= int(x) <= 9:
            if grid[int(x)-1] == " ":
                grid[int(x)-1] = assign[name_list[turn]]
                repeat = False
            else:
                print("There is already a symbol on this spot!")
        else:
            print("The number must be within the range 1-9!")

#Win conditions
def win_cond():
    global turn
    if grid[0] != " " and grid[0] == grid[3] and grid[3] == grid[6]:
        return "win"
    if grid[1] != " " and grid[1] == grid[4] and grid[4] == grid[7]:
        return "win"
    if grid[2] != " " and grid[2] == grid[5] and grid[5] == grid[8]:
        return "win"
    if grid[0] != " " and grid[0] == grid[1] and grid[1] == grid[2]:
        return "win"
    if grid[3] != " " and grid[3] == grid[4] and grid[4] == grid[5]:
        return "win"
    if grid[6] != " " and grid[6] == grid[7] and grid[7] == grid[8]:
        return "win"
    if grid[0] != " " and grid[0] == grid[4] and grid[4] == grid[8]:
        return "win"
    if grid[6] != " " and grid[6] == grid[4] and grid[4] == grid[2]:
        return "win"
    elif " " not in grid:
        return "draw"


    else:
        if turn == 0:
            turn = 1
        else:
            turn = 0
        return False

def reset():
    global name_list
    global assign
    global grid
    global turn

    assign = {}
    grid = []
    turn = 0
    for i in range(9):
        grid.append(" ")
    if changeName == True:
        name_list = []
    else:
        pass

#Win message
def win_msg():
    global changeName
    global m_repeat
    repeat = True
    answer = ["Y","y","N","n"]
    if win_cond() == "win":
        print(f"{name_list[turn]} won!")
    else:
        print("It's a draw!")
    while repeat:
        x = input("Play again? (Y/N): \n")
        print("\n"*50)
        if x not in answer:
            print("Sorry, I do not understand you.")
        elif x == "Y" or x == "y":
            n = input("Continue with the same names? (Y/N): \n")
            print("\n"*50)
            if n not in answer:
                print("Sorry, I do not understand you.")
            elif n == "Y" or n == "y":
                changeName = False
                break
            else:
                changeName = True
                break
        else:
            m_repeat = False
            print("Thank you for playing!")
            break

while m_repeat:
    if changeName:
        get_names()
    start_order()
    symbol_choice()
    while win_cond() == False:
        replace()
    else:
        win_msg()
        reset()
