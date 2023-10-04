# reading user's command line arguments
import sys
# display help message
import modules.help as help
# parsing commandline arguments
from modules.parse import parser

import modules.core as core

def main():
    if len(sys.argv) <= 1:
        help.help()
    else:
        try:
            parser(sys.argv[1:])
        except IndexError:
            print("Invalid argument count")
            help.help()
        except FileNotFoundError:
            print("non-existing group, group item or directory")
        except TypeError:
            print("Wrong type detected")
        except:
            print("unknown error occured")

if __name__ == "__main__":
    main()