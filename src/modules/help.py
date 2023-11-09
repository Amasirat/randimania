_HELP_MESSAGE = """help:

usage: <program name> <operation> <input parameters>(seperated by space)

Operations:
help, 0 input parameters:
    prints this page

add-group, 1 input parameter -> <name of group>:
    creates a new group to add your randomizable elements, for example: add-group art
    
add-elements, 2 or more input parameters -> <group name> <element 1> <element 2> ... <element n>:
    adds any number of elements to a pre-existing group

show-groups, no input parameters:
    show current existing groups

show-elements, 1 input parameter -> <group name>:
    shows elements of a group unrandomized

delete-group, 1 input parameter -> <group name>:
    deletes an existing group, WARNING All elements related to the group will be removed forever
    
delete-element, 2 input parameters -> <group name> <id of element gotten from show-elements>:
    deletes an element from a particular group

pull-random, 2 input parameters -> <group name> <number of elements desired as an integer>:
    pulls n number of random elements from one particular group
"""
def help():
    print(_HELP_MESSAGE)