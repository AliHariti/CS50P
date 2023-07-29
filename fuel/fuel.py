while True:
    try:
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        if x > y:
            pass
        else:
            tank =(x / y) * 100
            break
    except(ValueError, ZeroDivisionError):
        pass

if tank >= 99:
    print("F")
elif tank <= 1:
    print("E")
else:
    print(f"{round(tank)}%")
