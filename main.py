import sys
import modules.help as help
import modules.core as core
from modules.parse import parse_arg

def main():
    if len(sys.argv) <= 1:
        help.help()
    else:
        parse_arg(sys.argv[1:])


if __name__ == "__main__":
    main()