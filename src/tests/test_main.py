import os

groups = [g for g in os.listdir("src/groups/") if os.path.isfile(os.path.join("src/groups/", g))]
print(groups)