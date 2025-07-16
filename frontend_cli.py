# from ToDoModules.functions import get_todos, write_todos  
import ToDoModules.functions as tdmf
import time 

now = time.strftime("%a %d %b %Y, %H:%M:%S ")

print("it is now", now)
while True:
    user_action = input('Type add, show, edit, complete or exit:')
    user_action = user_action.strip()
        

    if user_action.startswith('add'): 
        todo = user_action[4:]
        
        #using with context manager allows for cleaner code and accidental
        #files being opened without being closed and thus causing problems
        
        todos = tdmf.get_todos()
            
        todos.append(todo +'\n')
        
        tdmf.write_todos(filepath="files/todos.txt",list_arg=todos)
            
        
    elif user_action.startswith('show'):
        #unless a file is already present, initialise a variable that opens the txt file otherwise will return an error assuming 
        #"show" is chosen upon .py file activation
        todos = tdmf.get_todos("files/todos.txt")
        
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)
            
    elif user_action.startswith('edit'):
        try:
            # print('Got it! here is your list of items as it stands....')
            number = int(user_action[5:])
            print(number)
            
            number = number - 1
            
            todos = tdmf.get_todos()
                
            print(todos)
                
            for index, item in enumerate(todos): 
                print(f"{index + 1}-{item.title().strip()}")
                
            # print("Please enter the item's corresponding index number you would like to modify..")
            #/todo_number = int(input("Enter here:"))
            # #below, we assume the user is not familiar with python indexing. So 
            # #we allow them to count from 1 rather than 0
            # /todo_number = todo_number - 1 
            new_todo = input("Enter a new to-do:")
            
            todos[number] = new_todo +'\n'
            
            tdmf.write_todos("files/todos.txt",todos)
           
        except ValueError:
            print("Your command is not valid!")
            continue
            
    elif user_action.startswith('complete'):
        try:   # /todo_number = int(input("Number of the to-do to complete: "))
            number = int(user_action[9:])
            todos = tdmf.get_todos()
            
            list_index = number - 1 
            todo_to_remove = todos[list_index].strip('\n')
            
            todos.pop(list_index)
            
            tdmf.write_todos("files/todos.txt",todos)
                
            message = f"To-do item {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no Item with that number!")
            continue
    elif user_action.startswith('exit'):
        print('Goodbye!!')
        break
    
    else:
        print("invalid command!")
    

