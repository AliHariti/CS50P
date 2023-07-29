import sys
from datetime import date
import inflect

p = inflect.engine()

def main():
    try:
        year, month, day = input("Date of Birth: ").split("-")
    except ValueError:
        sys.exit("Invalid Date")
    print(life_in_minutes(year, month, day))


def life_in_minutes(year, month, day):
    try:
        mydate = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid Date")

    today = date.today()
    diff_minutes = int((today - mydate).total_seconds() / 60)
    diff_min_Wrd = p.number_to_words(diff_minutes, andword="") + " minutes"
    return diff_min_Wrd.capitalize()


if __name__ == "__main__":
    main()