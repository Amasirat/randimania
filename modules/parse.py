from . import core
from . import help
OPERATIONS = [
    "add-group",
    "add-elements",
    "pull-random",
]
# parses arguments recieved as input
def parse_arg(arguments : list):
    if len(arguments) < 0:
        raise IndexError # meaning list is of invalid length
    match arguments[0]:
        case "add-group":
            if len(arguments) != 2:
                raise IndexError
            else:
                groupname = arguments[1]
                try:
                    core.create_group(groupname)
                except FileExistsError as error:
                    print("group already exists")
                else:
                    print(f"group {groupname} has been created...")
        case _:
            help.help()




