FILEPATH = "files/todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a text file and return a list of to-do items"""
    
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(list_arg, filepath=FILEPATH):
    """Write a to-do items list in a text file"""
    

    with open(filepath, "w") as file_local:
        file_local.writelines(list_arg)
        
if __name__ == "__main__":
    print("Modules activated")


