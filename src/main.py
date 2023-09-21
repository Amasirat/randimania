import sys
import modules.help as help
import modules.core as core
from modules.parse import parser

def main():
    if len(sys.argv) <= 1:
        help.help()
    else:
        try:
            parser(sys.argv[1:])
        except IndexError:
            print("Invalid argument count")
        except:
            print("unknown error occured")


if __name__ == "__main__":
    main()