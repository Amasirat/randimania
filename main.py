import sys
import modules.help as help
import modules.core as core
from modules.parse import parser

def main():
    if len(sys.argv) <= 1:
        help.help()
    else:
        parser(sys.argv[1:])


if __name__ == "__main__":
    main()