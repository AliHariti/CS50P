from validator_collection import checkers


def main():
    if check_email(input("What's your email address? ")):
        print("Valid")
    else:
        print("Invalid")


def check_email(s):
    return checkers.is_email(s)


if __name__ == "__main__":
    main()