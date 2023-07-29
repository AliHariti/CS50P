import argparse

parser = argparse.ArgumentParser(description="Just a Meow printer")
parser.add_argument("-n", default=1, help="number of meows printed", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")