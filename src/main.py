#!/usr/bin/env python3
# reading user's command line arguments
from multiprocessing import Value
import sys
# display help message
import modules.help as help
# parsing commandline arguments
from modules.parse import parser

def main():
    if len(sys.argv) <= 1:
        help.help()
    else:
        try:
            parser(sys.argv[1:])
        except IndexError:
            print("Invalid arguments")
            help.help()
        except FileNotFoundError:
            print("non-existing group, group item or directory")
        except ValueError:
            print("Wrong type gotten from user")
        except:
            print("unknown error occured")

if __name__ == "__main__":
    main()