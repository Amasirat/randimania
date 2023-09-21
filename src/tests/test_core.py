import modules.core as core
def test_row_counter_existing():
    try:
        core.row_counter("drawing")
    except FileNotFoundError as error:
        print(error)

def test_row_counter_non_existing():
    try:
        core.row_counter("audhaudg")
    except FileExistsError as error:
        print(error)