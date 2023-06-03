import termcolor as tc
import json, os

"""To-do-list functions"""
def todolist_write(todolist, statement=False):
    with open("todolist.json") as file:
        todolist_list = json.load(file)

    todolist_list[todolist] = statement

    with open("todolist.json", "w+") as file:
        json.dump(todolist_list, file)

def todolist_del(todolist):
    with open("todolist.json") as file:
        todolist_list = json.load(file)

    del todolist_list[todolist]

    with open("todolist.json", "w+") as file:
        json.dump(todolist_list, file)

def tick(todolist):
    with open("todolist.json") as file:
        todolist_list = json.load(file)

    if todolist in todolist_list:
        todolist_list[todolist] = True
    else:
        print("element not in list")

    with open("todolist.json", "w+") as file:
        json.dump(todolist_list, file)


def untick(todolist):
    with open("todolist.json") as file:
        todolist_list = json.load(file)

    if todolist in todolist_list:
        todolist_list[todolist] = False
    else:
        print("element not in list")

    with open("todolist.json", "w+") as file:
        json.dump(todolist_list, file)


def display_todolist():
    color_red = "on_red"
    color_green = "on_green"
    color_check_red = tc.colored("X", "black", color_red)
    color_check_green = tc.colored("0", "black", color_green)
    with open("todolist.json", "r") as file:
        todolist = json.load(file)
        print("General:")
        for do in todolist:
            if todolist[do] == True:
                print(color_check_green, end=" ")
                print(do)
            elif todolist[do] == False:
                print(color_check_red, end=" ")
                print(do)

"""set functions"""
def new_set(set_name):
    with open("todolist_set.json") as file:
        todolist_set_list = json.load(file)

    elements = []
    for element in todolist_set_list:
        elements.append(element)
    if set_name not in elements:
        todolist_set_list[set_name] = {}

    with open("todolist_set.json", "w+") as file:
        json.dump(todolist_set_list, file)

def del_set(set_name):
    with open("todolist_set.json") as file:
        todolist_set_list = json.load(file)
    elements = []
    for element in todolist_set_list:
        elements.append(element)
    if set_name in elements:
        del todolist_set_list[set_name]

    with open("todolist_set.json", "w+") as file:
        json.dump(todolist_set_list, file)

def open_set(set_name):
    while True:
        clear = lambda: os.system('cls')
        clear()
        color_red = "on_red"
        color_green = "on_green"
        color_check_red = tc.colored("X", "black", color_red)
        color_check_green = tc.colored("0", "black", color_green)
        with open("todolist_set.json", "r") as file:
            todolist_set = json.load(file)
            if set_name in todolist_set:
                print(f"{set_name} :")
                for do in todolist_set[set_name]:
                    if todolist_set[set_name][do] == True:
                        print(color_check_green, end=" ")
                        print(do)
                    elif todolist_set[set_name][do] == False:
                        print(color_check_red, end=" ")
                        print(do)
            else:
                print("pas present")
        key = input()
        command_set(set_name, key)
        if key == "quit":
            quit()
        if key == "back":
            break



def show_set():
    with open("todolist_set.json") as file:
        todolist_set_list = json.load(file)

    for set in todolist_set_list:
        print(set)
    print("\n")

    with open("todolist_set.json", "w+") as file:
        json.dump(todolist_set_list, file)

"""tasks in set functions"""
def add_set_task(set_name, task_name, statement=False):
    with open("todolist_set.json") as file:
        todolist_set_list = json.load(file)
    if task_name not in todolist_set_list[set_name]:
        todolist_set_list[set_name][task_name] = statement
    else:
        pass

    with open("todolist_set.json", "w+") as file:
        json.dump(todolist_set_list, file)

def del_set_task(set_name, task_name):
    with open("todolist_set.json") as file:
        todolist_set_list = json.load(file)

    del todolist_set_list[set_name][task_name]

    with open("todolist_set.json", "w+") as file:
        json.dump(todolist_set_list, file)

def tick_set_task(set_name, task_name):
    with open("todolist_set.json") as file:
        todolist_set_list = json.load(file)

    if task_name in todolist_set_list[set_name]:
        todolist_set_list[set_name][task_name] = True
    else:
        print("element not in set")

    with open("todolist_set.json", "w+") as file:
        json.dump(todolist_set_list, file)

def untick_set_task(set_name, task_name):
    with open("todolist_set.json") as file:
        todolist_set_list = json.load(file)

    if task_name in todolist_set_list[set_name]:
        todolist_set_list[set_name][task_name] = False
    else:
        print("element not in set")

    with open("todolist_set.json", "w+") as file:
        json.dump(todolist_set_list, file)

def open_help():
    with open("todolist_help.txt") as file:
        clear = lambda: os.system('cls')
        clear()
        for i in range(21):
            lines = file.readline()
            print(lines, end="")
        input()

"""commands writeable in the open set panel"""
def command_set(set_name, command="quit"):
    key_list = list(command)
    key_list_final = []
    name_set_list = []
    check_key = False
    for element in key_list:
        if element != " " and check_key is False:
            key_list_final.append(element)
        elif check_key is True:
            name_set_list.append(element)
        else:
            check_key = True
    name = "".join(name_set_list)
    command_final_set = "".join(key_list_final)
    while True:
        if command_final_set == "new":
            task = name
            add_set_task(set_name, task)
        if command_final_set == "del":
            task = name
            del_set_task(set_name, task)
        if command_final_set == "tick":
            task = name
            tick_set_task(set_name, task)
        if command_final_set == "untick":
            task = name
            untick_set_task(set_name, task)
        if command == "quit":
            quit()
        if command == "back":
            break
        if command == "help":
            open_help()


"""commands writeable in the general to-do-list"""
def command(command):
    command_list = list(command)
    command_list_final = []
    name_list = []
    check_command = False
    for element in command_list:
        if element != " " and check_command is False:
            command_list_final.append(element)
        elif check_command is True:
            name_list.append(element)
        else:
            check_command = True
    name = "".join(name_list)
    command_final = "".join(command_list_final)
    if command == "quit":
        quit()
    if command_final == "new":
        new_task = name
        todolist_write(new_task)
    if command_final == "del":
        del_task = name
        todolist_del(del_task)
    if command_final == "tick":
        tick_task = name
        tick(tick_task)
    if command_final == "untick":
        untick_task = name
        untick(untick_task)
    if command == "show set":
        clear = lambda: os.system('cls')
        clear()
        while True:
            """commands writeable in the show sets panel"""
            clear = lambda: os.system('cls')
            clear()
            print("set :")
            show_set()

            key = input()
            key_list = list(key)
            key_list_final = []
            name_set_list = []
            check_key = False
            for element in key_list:
                if element != " " and check_key is False:
                    key_list_final.append(element)
                elif check_key is True:
                    name_set_list.append(element)
                else:
                    check_key = True
            name_set = "".join(name_set_list)
            key_final_set = "".join(key_list_final)

            if key_final_set == "open":
                set_name = name_set
                open_set(set_name)
                clear = lambda: os.system('cls')
                clear()
            if key_final_set == "new":
                new_set_name = name_set
                new_set(new_set_name)
            if key_final_set == "del":
                set_name = name_set
                del_set(set_name)
            if key == "quit":
                quit()
            if key == "back":
                break
            if key == "help":
                open_help()
    if command == "help":
        open_help()

"""main function"""
def main():
    clear = lambda: os.system('cls')
    clear()
    while True:
        display_todolist()
        key = input()
        command(key)
        clear = lambda: os.system('cls')
        clear()

main()