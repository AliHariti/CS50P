months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    cleanDate()


def cleanDate():
    while True:
        date = input("Date: ")
        date = date.strip()
        try:
            if "," in date:
                month, day, year = date.split(" ")
                if month in months:
                    day = day.strip(",")
                    month = months.index(month) + 1
            else:
                month, day, year = date.split("/")
            if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
                break
        except ValueError:
            pass
    print(f"{year}-{int(month):02}-{int(day):02}")


main()
