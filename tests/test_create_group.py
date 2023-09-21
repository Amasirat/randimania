import modules.core as core

def test_default_create_group():
    try:
        core.create_group("drawing")
    except FileExistsError:
        print("group already exists")