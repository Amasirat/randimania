from modules.core import append_element

def test_append_element():
    try:
        append_element("line excercise", "drawing")
    except FileNotFoundError:
        print("group was not found")