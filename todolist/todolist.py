import termcolor as tc
import os, json

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
class Todolist:
    def __init__(self, path, mode):
        self.path = path
        self.running = True
        self.mode = mode
        self.sets = Set()
        
    def show(self, help=None):
        if help == "help":
            with open("todolist_help.txt", "r+") as data:
                text = data.readlines()
                for line in text:
                    print(line, end="")
        else:
            color_check_red = tc.colored("X", "white", "on_red")
            color_check_green = tc.colored("0", "white", "on_green")
            print(f"{self.mode} panel")
            with open(self.path, "r+") as data:
                todolist = json.load(data)
                i = 0
                for elements in todolist[self.mode]:
                    if todolist[self.mode][elements] == True:
                        print(i, color_check_green, end=" ")
                        print(elements)
                        i += 1
                    else:
                        print(i, color_check_red, end=" ")
                        print(elements)
                        i += 1

    def add(self, element):
        with open(self.path, "r+") as data:
            todolist = json.load(data)

            if type(element) == list:
                todolist[self.mode][" ".join(element)] = False
            else:
                todolist[self.mode][element] = False
                
        with open(self.path, "w+") as data:
            json.dump(todolist, data)

    def supr(self, element):
        with open(self.path, "r+") as data:
            todolist = json.load(data)

            if type(element) == list:
                if " ".join(element) in todolist[self.mode]:
                    del todolist[self.mode][" ".join(element)]
            else:
                if element in todolist[self.mode]:
                    del todolist[self.mode][element]
            
        with open(self.path, "w+") as data:
            json.dump(todolist, data)

    def supr_num(self, element):
        with open(self.path, "r+") as data:
            todolist = json.load(data)

            todolist_ = list(todolist[self.mode])
            element = int(element)
            if element <= len(todolist[self.mode]):
                del todolist[self.mode][todolist_[element]]
                        
        with open(self.path, "w+") as data:
            json.dump(todolist, data)

    def tick(self, element):
        with open(self.path, "r+") as data:
            todolist = json.load(data)

            if type(element) == list:
                if " ".join(element) in todolist[self.mode]:
                    todolist[self.mode][" ".join(element)] = True
            else:
                if element in todolist[self.mode]:
                    todolist[self.mode][element] = True

            
        with open(self.path, "w+") as data:
            json.dump(todolist, data)

    def tick_num(self, element):
        with open(self.path, "r+") as data:
            todolist = json.load(data)

            todolist_ = list(todolist[self.mode])
            element = int(element)
            if element <= len(todolist[self.mode]):
                todolist[self.mode][todolist_[element]] = True
                        
        with open(self.path, "w+") as data:
            json.dump(todolist, data)
            
    def untick(self, element):
        with open(self.path, "r+") as data:
            todolist = json.load(data)

            if type(element) == list:
                if " ".join(element) in todolist[self.mode]:
                    todolist[self.mode][" ".join(element)] = False
            else:
                if element in todolist[self.mode]:
                    todolist[element] = False
            
        with open(self.path, "w+") as data:
            json.dump(todolist, data)

    def untick_num(self, element):
        with open(self.path, "r+") as data:
            todolist = json.load(data)

            todolist_ = list(todolist[self.mode])
            element = int(element)
            if element <= len(todolist[self.mode]):
                todolist[self.mode][todolist_[element]] = False
                        
        with open(self.path, "w+") as data:
            json.dump(todolist, data)

    def move(self, element, new_location):
        with open(self.path, "r+") as data:
            todolist = json.load(data)

            todolist_ = list(todolist[self.mode])
            element = int(element)
            new_location = int(new_location)
            if element <= len(todolist[self.mode]):
                key_pop = todolist_[element]
                value_pop = todolist[self.mode].pop(todolist_[element])
                items = list(todolist[self.mode].items())
                items.insert(new_location, (key_pop, value_pop))
                todolist[self.mode] = dict(items)
                
        with open(self.path, "w+") as data:
            json.dump(todolist, data)

    


    def run(self):
        while self.running:
            clear()
            self.show()
            input_cmd = input().split(" ")
            if input_cmd[0] == "add" or input_cmd[0] == "new":
                self.add(input_cmd[1:None])
                
            if input_cmd[0] == "del":
                self.supr(input_cmd[1:None])

            if input_cmd[0] == "tick":
                self.tick(input_cmd[1:None])

            if input_cmd[0] == "untick":
                self.untick(input_cmd[1:None])

            if input_cmd[0] == "deln":
                self.supr_num(input_cmd[1])

            if input_cmd[0] == "tickn":
                self.tick_num(input_cmd[1])

            if input_cmd[0] == "untickn":
                self.untick_num(input_cmd[1])

            if input_cmd[0] == "move":
                self.move(input_cmd[1], input_cmd[2])

            if input_cmd[0] == "sets" or input_cmd[0] == "set":
                self.sets.run()

            if input_cmd[0] == "help":
                self.show("help")
                input("\npress enter to quit")

            if input_cmd[0] == "return":
                break
            
            if input_cmd[0] == "q" or input_cmd[0] == "quit":
                quit()
            
class Set:
    def __init__(self):
        self.path = "todolist.json"
        self.running = True

        
    def show(self, help=None):
        if help == "help":
            with open("todolist_help.txt", "r+") as data:
                text = data.readlines()
                for line in text:
                    print(line, end="")
        else:
            print("Sets")
            with open(self.path, "r+") as data:
                todolist = json.load(data)
                i = 0
                for elements in todolist:
                    if todolist[elements] == True:
                        print(i, elements)
                        i += 1
                    else:
                        print(i, elements)
                        i += 1
    
    def add(self, element):
        with open(self.path, "r+") as data:
            todolist = json.load(data)

            if type(element) == list:
                todolist[" ".join(element)] = {}
            else:
                todolist[element] = {}
                
        with open(self.path, "w+") as data:
            json.dump(todolist, data)

    def supr(self, element):
        with open(self.path, "r+") as data:
            todolist = json.load(data)

            if type(element) == list:
                if " ".join(element) in todolist and " ".join(element) != "general":
                    del todolist[" ".join(element)]
            else:
                if element in todolist and element != "general":
                    del todolist[element]
            
        with open(self.path, "w+") as data:
            json.dump(todolist, data)

    def supr_num(self, element):
        with open(self.path, "r+") as data:
            todolist = json.load(data)

            todolist_ = list(todolist)
            element = int(element)
            if element <= len(todolist):
                if todolist[todolist_[element]] != "general":
                    del todolist[todolist_[element]]
                        
        with open(self.path, "w+") as data:
            json.dump(todolist, data)

    def move(self, element, new_location):
        with open(self.path, "r+") as data:
            todolist = json.load(data)

            todolist_ = list(todolist)
            element = int(element)
            new_location = int(new_location)
            if element <= len(todolist):
                key_pop = todolist_[element]
                value_pop = todolist.pop(todolist_[element])
                items = list(todolist.items())
                items.insert(new_location, (key_pop, value_pop))
                todolist = dict(items)
                
        with open(self.path, "w+") as data:
            json.dump(todolist, data)

    def open(self, set_):
        with open(self.path, "r+") as data:
            todolist = json.load(data)
            
            if set_ in todolist:
                Todolist("todolist.json", set_).run()

    def open_num(self, set_num):
        with open(self.path, "r+") as data:
            todolist = json.load(data)

            todolist_ = list(todolist)
            if set_num <= len(todolist):
                Todolist("todolist.json", todolist_[set_num]).run()

            
    def run(self):
        while self.running:
            clear()
            self.show()
            input_cmd = input().split(" ")
            if input_cmd[0] == "add" or input_cmd[0] == "new":
                self.add(input_cmd[1:None])
                
            if input_cmd[0] == "del":
                self.supr(input_cmd[1:None])

            if input_cmd[0] == "deln":
                self.supr_num(input_cmd[1])

            if input_cmd[0] == "move":
                self.move(input_cmd[1], input_cmd[2])

            if input_cmd[0] == "open":
                self.open(" ".join(input_cmd[1:None]))

            if input_cmd[0] == "openn":
                self.open_num(int(input_cmd[1]))

            if input_cmd[0] == "help":
                self.show("help")
                input("\npress enter to quit")
            
            if input_cmd[0] == "return":
                break
            
            if input_cmd[0] == "q" or input_cmd[0] == "quit":
                quit()

            
    
        


Todolist("todolist.json", "general").run()








