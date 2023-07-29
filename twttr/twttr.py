text = input("input: ")
print("Output: ", end="")
forbiden = ["a", "e", "i", "o", "u"]

for w in text:
    if w.lower() not in forbiden:
     print(w, end="")

print()
