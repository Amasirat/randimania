import modules.core as core

try:
    core.append_element("line excercise", "drawing")
except FileNotFoundError:
    print("group was not found")