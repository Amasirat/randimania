_help_message = """help:
usage: <program name> <operation> <input parameters>(seperated by space)

Operations:
add-group, 1 input parameter -> <name of group>
add-elements, 2 or more input parameters -> <group name> <element 1> <element 2> ... <element n> 
pull-random, 2 input parameters -> <group name> <number of elements desired> 

"""

def help():
    print(_help_message)