# Randomizer

Personal simple program that randomizers n number of elements.

# System
Randomized elements are structured as different groups. The user creates groups and inputs elements into them, and the program stores them inside a csv file. When the user asks for n elements back, the program will randomize and show them to the user.

# Usage
\<program name\> \<operation\> \<input parameters\>(seperated by space)

Operations:

add-group, 1 input parameter -> \<name of group\>

add-elements, 2 or more input parameters -> \<group name\> \<element 1\> \<element 2\> ... \<element n\> 

show-groups, 1 input parameter -> \<name of group\>

show-elements, 1 input parameter -> \<group name\>

delete group, 1 input parameter -> \<group name\>

delete elements, 2 input parameres -> \<group name\> \<element\>

pull-random, 2 input parameters -> \<group name\> \<number of elements desired as an integer\>

# Documentation
Groups are in basic terms just names for files in the system. When creating a group, a csv file will be created wth elements of each groups being appended to these files along with an id assigned to them. The first element of each of these files will always be the name of the group.

By default, these files are stored in groups/ directory in source file and should be in use **only** by the program. Meaning no addition or removal or any other sort of edits should be done to these files and the program should handle everything itself.