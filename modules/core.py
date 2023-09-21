from . import _global
import os
# opening a group file
def create_group(groupname, group_dir = _global.GROUP_DIR):       
# necessary condition checking needed later
    dir = ""
    try:
        os.mkdir(group_dir)
        dir = f"{group_dir}{groupname}.txt"
    except FileExistsError:
        dir = f"{group_dir}{groupname}.txt"

    with open(dir, "w") as file:
        file.write(groupname)
    