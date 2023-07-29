grocery = dict()

while True:
    try:
        item = input().upper()
    except EOFError:
        print()
        break
    if item in grocery:
        grocery[item] += 1
    else:
        grocery[item] = 1

for key in sorted(grocery.keys()):
    print(grocery[key], key)
