# Randimania

Simple command-line tool that randomizes n number of elements.

# System

Randomized elements are structured as different groups. The user creates groups and inputs elements into them, then the program stores them inside a csv file named after that group. When the user asks for n elements back, the program will randomize and show them to the user.

# Usage

\<program name\> \<operation\> \<input parameters\>(seperated by space)

Operations:

add-group, 1 input parameter -> \<name of group\>

add-elements, 2 or more input parameters -> \<group name\> \<element 1\> \<element 2\> ... \<element n\>

show-groups, no input parameters

show-elements, 1 input parameter -> \<group name\>

delete group, 1 input parameter -> \<group name\>

delete element, 2 input parameres -> \<group name\> \<element\>

pull-random, 2 input parameters -> \<group name\> \<number of elements desired as an integer\>

# Documentation

Groups are in basic terms just names for files in the system. When creating a group, a csv file will be created wth elements of each groups being appended to these files along with an id assigned to them. The first element of each of these files will always be the name of the group.

By default, these files are stored in groups/ directory in source file and should be in use **only** by the program. Meaning no addition or removal or any other sort of edits should be done to these files manually and the program should handle everything by itself.

Project's directory structures is this:
inside the src directory, there is the main.py script, which is the main program. There are also the tests and modules directories. tests is delegated to unit tests and modules contains the main functionality of the program.

The modules package contains help, parse, and core modules.

----help display's a help message on screen

----parse contains the parser() function that parses command-line arguments

----core contains coe functionality of the program. pulling random elements, writing and reading from csv files, etc...
