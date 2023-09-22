import modules.core as core
def test_row_counter_existing():
    try:
        core.row_counter("drawing")
    except FileNotFoundError as error:
        print(error)
        
def test_random_pull():
    core.random_pull("drawing")
