def main():
    greeting = input("greeting: " ).lower().strip()
    print(f"${value(greeting)}")


def value(greeting):
    if greeting.startswith("hello"):
        return(0)
    elif greeting.startswith("h"):
        return(20)
    else:
        return(10)


if __name__ == "__main__":
    main()