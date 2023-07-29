def main():
    text = input("Input: ")
    print(f"Output: {shorten(text)}")


def shorten(word):
    forbiden = "aeiou"
    new_word = ""
    for w in word:
        if not w.lower() in forbiden:
            new_word += w
    return new_word


if __name__ == "__main__":
    main()