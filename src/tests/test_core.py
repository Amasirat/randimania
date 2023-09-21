import modules.core as core
def test_row_counter_existing():
    try:
        core.row_counter("drawing")
    except FileNotFoundError as error:
        print(error)
