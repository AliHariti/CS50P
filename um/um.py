import re


def main():
    print(count(input("Text: ")))


def count(s):
    tocount = re.findall(r'\b(u|U)m\b', s)
    return len(tocount)


if __name__ == "__main__":
    main()