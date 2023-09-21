from . import core
from . import _global
from . import help
import os

# function for add-group arg
def arg_add_group(arg):
    groupname = arg
    try:
        core.create_group(groupname)
    except FileExistsError:
        print("group already exists")
    else:
        print(f"group {groupname} has been created...")

# function for delete-group arg
def arg_delete_group(arg):
    groupname = arg
    dir = f"{_global.GROUP_DIR}{groupname}.csv"
    if not os.path.isfile(dir):
        raise FileNotFoundError
    
    print(f"Are you sure you want to delete group '{arg}'?")
    while True:
        usr_input = input("Deleting this group will also delete all its elements[y/n]:")
        usr_input.lower().rstrip()

        match usr_input:
            case 'y':
                os.remove(dir)
                print("group successfuly deleted")
                return
            case 'n':
                return
            case _:
                print("invalid input, try again")
            

# parses arguments recieved as input
def parser(arguments : list):
    if len(arguments) < 0:
        raise IndexError # meaning list is of invalid length
    match arguments[0]:
        case "add-group":
            if len(arguments) != 2:
                raise IndexError
            else:
                arg_add_group(arguments[1])
        case "delete-group":
            if len(arguments) != 2:
                raise IndexError
            arg_delete_group(arguments[1])
        case "show-groups":
            pass

        case _:
            help.help()





