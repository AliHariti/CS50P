import json
import requests
import sys


def main():
    convertBitcoin()


def isfloat(s):
    try:
        if float(s):
            return True
    except ValueError:
        return False


def convertBitcoin():
    try:
        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")
        elif not isfloat(sys.argv[1]):
            sys.exit("Command-line argument is not a number")

        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        price = float(sys.argv[1]) * o["bpi"]["USD"]["rate_float"]
        print(f"${price:,.4f}")
    except requests.RequestException:
        pass


if __name__ == "__main__":
    main()
