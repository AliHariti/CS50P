import inflect


p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ").strip()
    except EOFError:
        break
    if name != "":
        names.append(name)

print(f"\nAdieu, adieu, to {p.join(names)}")
