import sys
import modules.help as help
import modules.core as core

def main():
    try:
        core.append_element("ghost lines", "drawing")
    except FileNotFoundError as err:
        print(err)
    #if len(sys.argv) <= 1:
        #help.help()

if __name__ == "__main__":
    main()