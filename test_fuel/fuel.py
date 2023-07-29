def main():
    percentage = convert(input("Fraction: "))
    print(gauge(percentage))


def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if x > y:
                raise ValueError
            else:
                tank = round((x / y) * 100)
                return tank
        except(ValueError, TypeError, ZeroDivisionError):
            fraction = input("Fraction: ")
            pass


def gauge(percentage):
    if percentage >= 99:
        return("F")
    elif percentage <= 1:
        return("E")
    else:
        return(f"{percentage}%")


if __name__ == "__main__":
    main()
