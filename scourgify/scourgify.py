import sys
import csv


def main():
    check_valid()
    beforelist = read_beforecsv(sys.argv[1])
    write_aftercsv(beforelist, sys.argv[2])


def check_valid():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")


def read_beforecsv(myfile):
    try:
        charachters = []
        with open(myfile) as file:
            reader = csv.DictReader(file)
            for row in reader:
                charachters.append(row)
    except FileNotFoundError:
        sys.exit(f"Could not read {myfile}")
    return charachters


def write_aftercsv(beforelist, afterfile):
    with open(afterfile, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first":"first", "last": "last", "house": "house"})
        for charachters in beforelist:
            last, first = charachters['name'].split(', ')
            house = charachters['house']
            writer.writerow({"first":first, "last": last, "house": house})


if __name__ == "__main__":
    main()
