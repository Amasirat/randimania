_help_message = """help:
usage: <program name> <operation> <input parameters>(seperated by space)

Operations:
add-group, 1 input parameter -> <name of group>
add-elements, 2 or more input parameters -> <group name> <element 1> <element 2> ... <element n> 

show-groups, no input parameters 
show-elements, 1 input parameter -> <group name>

delete-group, 1 input parameter -> <group name>
delete-element, 2 input parameres -> <group name> <element>

pull-random, 2 input parameters -> <group name> <number of elements desired as an integer>
"""

def help():
    print(_help_message)