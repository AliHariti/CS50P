word = input("Word: ")
for c in word:
    if c.isupper():
        c = "_" + c.lower()
    print(c, end="")
print()
