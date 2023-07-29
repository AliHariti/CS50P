import sys

from PIL import Image, ImageOps


def main():
    check_valid()
    try:
        image = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Input does not exist")
    image = ImageOps.fit(image, shirt.size)
    image.paste(shirt, shirt)
    image.save(sys.argv[2])


def check_valid():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    suffix = ("png", "jpg", "jpeg")
    if not sys.argv[1].lower().endswith(suffix):
        sys.exit("Invalid input")
    if not sys.argv[2].lower().endswith(suffix):
        sys.exit("Invalid output")

    ext1 = sys.argv[1].split(".")[1]
    ext2 = sys.argv[2].split(".")[1]
    if ext1.lower() != ext2.lower():
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
