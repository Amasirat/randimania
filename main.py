import sys
import modules.help as help

def main():
    if len(sys.argv) <= 1:
        help.help()

if __name__ == "__main__":
    main()