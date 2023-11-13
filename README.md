# Randimania

Simple command-line tool that stores and randomizes any number of elements written in python for the linux command line.

Currently there are no plans for windows or mac support.

# System

Each element is a part of a particular group which the user has to create when using the program for the first time. Then any other operations are done on elements which are a part of these groups.

# Usage

usage: 'program name' 'operation' 'input parameters'(seperated by space)

Operations:

help, 0 input parameters:

    prints help message

add-group, 1 input parameter -> 'name of group':

    creates a new group to add your randomizable elements, for example: add-group art
    
add-elements, 2 or more input parameters -> 'group name' 'element 1' 'element 2' ... 'element n':

    adds any number of elements to a pre-existing group

show-groups, no input parameters:

    show current existing groups

show-elements, 1 input parameter -> 'group name':

    shows elements of a group unrandomized

delete-group, 1 input parameter -> 'group name':

    deletes an existing group, WARNING All elements related to the group will be removed forever
    
delete-element, 2 input parameters -> 'group name' 'element':

    deletes an element from a particular group

pull-random, 2 input parameters -> 'group name' 'number of elements desired as an integer':

    pulls n number of random elements from one particular group

# Documentation

Groups are in basic terms just names for files in the system. When creating a group, a csv file will be created wth elements of each groups being appended to these files along with an id assigned to them. The first row of the csv files is "id, element".

By default, these files are stored in ~/.config/groups/ directory in source file and should be in use **only** by the program. Meaning no addition or removal or any other sort of edits should be done to these files manually and the program should handle everything by itself.

Project's directory structure is this:
inside the src directory, there is the main.py script, which is the main program script. There are also the tests and modules directories. tests is delegated to unit tests and modules contains the main functionality of the program and is a package.

The modules package contains help, parse, and core modules.

----help has function that displays a help message on screen

----parse contains the parser() function that parses command-line arguments and accesses core functions to perform needed tasks.

----core contains core functionality of the program. pulling random elements, writing and reading from csv files, etc...

main.py script calls parser, while parser can access core functions to perform the required fuction and then return back to caller. Suffice it to say, any error handling takes place inside the main.py script, after any exceptions are raised and through the core or parser modules reach the main.
