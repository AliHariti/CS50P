import sys


def main():
    check_valid()
    print(lines_calc(sys.argv[1]))


def check_valid():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if not sys.argv[1].endswith('.py'):
        sys.exit("Not a Python file")


def lines_calc(myfile):
    try:
        with open(myfile) as file:
            count = 0
            for line in file:
                if line.lstrip():
                    if not line.lstrip().startswith('#'):
                        count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    return(count)


if __name__ == "__main__":
    main()
