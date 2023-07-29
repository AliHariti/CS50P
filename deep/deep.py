answer = input("answer: ").lower().strip()
match answer:
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _:
        print("No")
