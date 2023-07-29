def main():
    timenow = input("What time is it? ")
    timenow = convert(timenow)

    if 7 <= timenow <= 8:
        print("breakfast time")
    elif 12 <= timenow <= 13:
        print("lunch time")
    elif 18 <= timenow <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)

    # Chalenge :  support for 12-hour times
    if "a" in minutes:
        minutes = minutes.partition(" ")[0]
    elif "p" in minutes:
        minutes = minutes.partition(" ")[0]
        hours = hours + 12
    # end chalenge
    minutes = float(minutes) / 60
    return(hours + minutes)


if __name__ == "__main__":
    main()