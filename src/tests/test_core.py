import modules.core as core
import os
def test_create_group():
    try:
        core.create_group("b")
    except FileExistsError:
        print("exists")
    assert(os.path.isfile(core.GROUP_DIR + "a.csv"))
        
def test_row_counter():
    try:
        core.create_group("row_counter_test")
        core.append_element("row_counter_test", "sd")
    except FileExistsError:
        print("exists")
    count: int = core.row_counter("sd")
    assert(count == 2)
    

def test_append_element():
    pass

def test_show_elements():
    pass

def test_return_group():
    pass

def test_random_pull():
    pass
    
def test_access_elements():
    pass

def test_delete_element():
    pass

def test_random_pull_music():
    pass
