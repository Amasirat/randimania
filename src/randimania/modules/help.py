# Copyright (c) 2024 Amasirat

# Permission is hereby granted, free of charge, to any person obtaining 
# a copy of this software and associated documentation files (the "Software"), 
# to deal in the Software without restriction, including without limitation the rights to use, copy, modify, 
# merge, publish, distribute, 
# sublicense, and/or sell copies of the Software, 
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies 
# or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE 
# AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
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