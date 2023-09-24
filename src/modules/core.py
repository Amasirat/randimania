import csv
import os
import random
GROUP_DIR : str = "src/groups/"
# opening a group file
def create_group(groupname : str):
    dir = f"{GROUP_DIR}{groupname}.csv"
    if not os.path.isdir(GROUP_DIR):    
        os.mkdir(GROUP_DIR)
    elif os.path.isfile(dir):
        raise FileExistsError
# open a file and write the first line
    with open(dir, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "element"])
        writer.writerow({"id": "id", "element": "elements"})

# this function only counts existing rows in a csv group file, INCLUDING the 0th row
def row_counter(group) -> int:
# checking if directory exists
    dir: str = f"{GROUP_DIR}{group}.csv"
    if not os.path.isfile(dir):
        raise FileNotFoundError
# starting couting process
    count : int = 0
    with open(dir, "r") as read:
        reader = csv.reader(read)
        count += sum(1 for _ in reader)
    return count

# appends an element to an existing group
# rasies FileNotFoundError in the case where group.csv was not found
def append_element(element: str, group : str):
    dir = f"{GROUP_DIR}{group}.csv"
    row_count = row_counter(group)

    if os.path.isfile(dir):
        with open(dir, "a") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "element"])
            writer.writerow({"id": row_count, "element": element})
    else:
        raise FileNotFoundError

# show elements of a group to user
def show_elements(group : str):
    dir = f"{GROUP_DIR}{group}.csv"
    # raise exception to caller if group file was not found
    if not os.path.isfile(dir):
        raise FileNotFoundError
    
    # exit function if there are no elements
    if row_counter(group) == 1:
        print(f"the group '{group}' has no elements")
        return
    # empty list to store elements from the file
    elements = []

    with open(dir, "r") as file:
        reader = csv.DictReader(file, fieldnames=["id", "element"])
        for row in reader:
            if row["id"] == "id":
                continue
            elements.append(row["element"])
    
    print(f"elements of {group}:")
    for item in elements:
        print(f"-{item}")

# show groups
def show_groups():
    # appending file names in global directory to groups 
    # if they are files in order to future proof
    groups = [g for g in os.listdir(GROUP_DIR) 
        if os.path.isfile(os.path.join(GROUP_DIR, g))
    ]
    # if groups turns out empty
    if not groups:
        print("No groups exist")
    
    for item in groups:
       group, _ =  item.split('.')
       print(f"--{group}")
       
# return a random element given a group
def random_pull(group : str) -> str:
    dir = os.path.join(GROUP_DIR, f"{group}.csv")
    if not os.path.isfile(dir):
        raise FileNotFoundError

    row_count = row_counter(group)
    return random.randint(1, row_count)

# given an id number it will return the element from the group
def access_element(group: str, id_num : int):
    dir = os.path.join(GROUP_DIR, f"{group}.csv")
    if not os.path.isfile(dir):
        raise FileNotFoundError
# loop to find element in csv file
    with open(dir, "r") as file:
        reader = csv.DictReader(file, fieldnames=["id", "element"])
        for row in reader:
            if row["id"] == "id":
                continue
        
            if int(row["id"]) == id_num: 
                return row["element"] 
    
        