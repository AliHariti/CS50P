def main():
    text = input("Enter your text: ")
    convert(text)

def convert(words):
    words = words.replace(":)", "🙂")
    words = words.replace(":(", "🙁")
    print(words)

main()