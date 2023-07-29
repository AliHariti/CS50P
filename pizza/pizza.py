import sys
import csv
from tabulate import tabulate


def main():
    check_valid()
    print(format_ASCII(sys.argv[1]))


def check_valid():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")



def format_ASCII(myfile):
    try:
        menu = []
        with open(myfile) as file:
            reader = csv.DictReader(file)
            for row in reader:
                menu.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
    return(tabulate(menu, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
