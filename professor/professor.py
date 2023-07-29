import random


def main():
    level = get_level()
    score = score_calc(level)
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            number = int(input("Level: "))
            if number in [1, 2, 3]:
                break
        except ValueError:
            pass
    return number


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


def result_test(x, y):
    test = 3
    while test > 0:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                test -= 1
                print("EEE")
        except ValueError:
            test -= 1
            print("EEE")
    print(f"{x} + {y} = {x + y}")
    return False


def score_calc(level):
    score = 10
    for _ in range(10):
        x, y = generate_integer(level)
        if not result_test(x, y):
            score -= 1
    return score


if __name__ == "__main__":
    main()
