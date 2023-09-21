from . import _global
import csv
import os

# opening a group file
def create_group(groupname : str):
    dir = f"{_global.GROUP_DIR}{groupname}.csv"
    if not os.path.isdir(_global.GROUP_DIR):    
        os.mkdir(_global.GROUP_DIR)
    elif os.path.isdir(dir):
        raise FileExistsError
# open a file and write the first line
    with open(dir, "w") as file:
        writer = csv.DictWriter(file, fieldnames={"id", "element"})
        writer.writerow({"id": 0, "element": groupname})

# this function only counts existing rows in a csv group file, INCLUDING the 0th row
# containing the groups's name
def row_counter(file) -> int:
    count : int = 0
    dir: str = f"{_global.GROUP_DIR}{file}.csv"
    with open(dir, "r") as read:
        reader = csv.reader(read)
        count += sum(1 for _ in reader)
    return count

# appends an element to an existing group
# rasies FileNotFoundError in the case where group.csv was not found
def append_element(element: str, group : str):
    dir = f"{_global.GROUP_DIR}{group}.csv"
    row_count = row_counter(group)
    
    if os.path.isfile(dir):
        with open(dir, "a") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "element"])
            writer.writerow({"id": row_count, "element": element})
    else:
        raise FileNotFoundError