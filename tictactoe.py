name_list = []
assign = {}
grid = []
for i in range(9):
    grid.append(" ")

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

def start_order():
    repeat = True
    answer = ["Y","y","N","n"]

    while repeat:
        start = input(f"Would you like to start first, {name_list[0]}? (Y/N): \n")
        print("\n"*50)
        if start not in answer:
            print("Sorry, I do not understand you.")
        else:
            if start == "Y" or "y":
                return True
            else:
                return False

def symbol_choice():
    repeat = True
    answer = ["X","x","O","o"]

    while repeat:
        start = input(f"Choose your symbol, {name_list[0]}. (X/O): \n")
        print("\n"*50)
        if start not in answer:
            print("Sorry, I do not understand you.")
        else:
            if start == "X" or "x":
                #assign X to namelist[0], O to namelist[1]
                symbol = ["X","O"]
                repeat = False

            else:
                #assign O to namelist[0], X to namelist[1]
                symbol = ["O","X"]
                repeat = False
    global assign
    assign = dict(zip(name_list,symbol))

def show_grid():
    print(" "+f"{grid[6]}"+" | "+f"{grid[7]}"+" | "+f"{grid[8]}")
    print("-"*11)
    print(" "+f"{grid[3]}"+" | "+f"{grid[4]}"+" | "+f"{grid[5]}")
    print("-"*11)
    print(" "+f"{grid[0]}"+" | "+f"{grid[1]}"+" | "+f"{grid[2]}")


get_names()
start_order()
symbol_choice()
print(assign)
