import csv
import os
import random
GROUP_DIR : str = "src/groups/"
# opening a group file
def create_group(groupname : str) -> None:
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
def append_element(element: str, group : str) -> None:
    dir = f"{GROUP_DIR}{group}.csv"
    row_count = row_counter(group)

    if os.path.isfile(dir):
        with open(dir, "a") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "element"])
            writer.writerow({"id": row_count, "element": element})
    else:
        raise FileNotFoundError

# show elements of a group to user
def show_elements(group : str) -> list:
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
    return elements

# show groups
def return_groups() -> list:
    # appending file names in global directory to groups 
    # if they are files in order to future proof
    groups = [g for g in os.listdir(GROUP_DIR) 
        if os.path.isfile(os.path.join(GROUP_DIR, g))
    ]
    
    return groups
# delete an element given a group and id number
# return a random element given a group
def random_pull(group : str) -> str:
    dir = os.path.join(GROUP_DIR, f"{group}.csv")
    if not os.path.isfile(dir):
        raise FileNotFoundError

    row_count = row_counter(group)
    return random.randint(1, row_count - 1)

# given an id number it will return the element from the group
def access_element(group: str, id_num : int) -> str:
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
            
# delete element given a group and id number
def delete_element(group: str, id : int):
    dir = os.path.join(GROUP_DIR, f"{group}.csv")
    if not os.path.isfile(dir):
        raise FileNotFoundError
# if id number is greater than the number of items in group, stop procedure
    if row_counter(group) < id:
        raise FileNotFoundError
    
    items = []
    with open(dir, "r") as file:
        reader = csv.DictReader(file, fieldnames=["id", "element"])
        for row in reader:
            items.append({"id": row["id"], "element": row["element"]})
            
    index : int = 1 #a list of elements from groups always starts at 1
    while index <= len(items) - 1:

        if int(items[index]["id"]) == id:
            items.remove(items[index])
            continue
            
        if int(items[index]["id"]) != index:
            items[index]["id"] = str(index)
        
        index += 1
    
    with open(dir, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "element"])
        for item in items:
            writer.writerow(item)

    return items