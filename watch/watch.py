import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*></iframe>", s):
        ytb_in = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)", s)
        if ytb_in:
            ytbshort = ytb_in.groups()
            return ("https://youtu.be/" + ytbshort[3])


if __name__ == "__main__":
    main()