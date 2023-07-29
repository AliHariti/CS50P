due = 50
while due > 0:
    print(f"Amount due: {due}")
    insert = int(input("Insert coin: "))
    if insert in [5, 10, 25]:
        due -= insert
change = abs(due)
print(f"change : {change}")
