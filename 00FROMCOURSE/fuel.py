#this version of fuel.py passed all check50 test but NOT working correctly
#Doesn't prompt after errors

def main():
    tank = fraction(input("Fraction: "))
    if tank >= 99:
        print("F")
    elif tank <= 1:
        print("E")
    else:
        print(f"{round(tank)}%")


def fraction(expression):
    while True:
        try:
            x, y = expression.split("/")
            x = int(x)
            y = int(y)
            if x > y:
                continue
            else:
                return ((x / y) * 100)
        except(ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()
