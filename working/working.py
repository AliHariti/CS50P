import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    timeformat = re.search(r"^([0-9][0-2]?):?([0-5][0-9])? ([A-P]M) to ([0-9][0-2]?):?([0-5][0-9])? ([A-P]M)$", s)
    if timeformat:
        if int(timeformat.group(1)) > 12 or int(timeformat.group(4)) > 12:
            raise ValueError
        fptf = convertion(timeformat.group(1), timeformat.group(2), timeformat.group(3))
        sptf = convertion(timeformat.group(4), timeformat.group(5), timeformat.group(6))
        newformat = fptf + " to " + sptf
        return newformat
    else:
        raise ValueError


def convertion(hour, minutes, pmam):
    """ newhour = 0
    newminutes = 0 """
    if pmam == "PM":
        if int(hour) == 12:
            newhour = 12
        else:
            newhour = int(hour) + 12
    else:
        if int(hour) == 12:
            newhour = 0
        else:
            newhour = int(hour)
    if minutes == None:
        newminutes = ":00"
        newtime = f"{newhour:02}" + newminutes
    else:
        newtime = f"{newhour:02}" + ":" + minutes

    return newtime


if __name__ == "__main__":
    main()