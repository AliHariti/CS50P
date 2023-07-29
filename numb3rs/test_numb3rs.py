from numb3rs import validate

def main():
    test_long()
    test_range()


def test_long():
    assert validate(r"255.122.10.1") == True
    assert validate(r"255.122.10") == False
    assert validate(r"255.122.") == False
    assert validate(r"255") == False


def test_range():
    assert validate(r"255.255.255.255") == True
    assert validate(r"256.255.255.255") == False
    assert validate(r"255.256.255.255") == False
    assert validate(r"255.255.256.255") == False
    assert validate(r"255.255.255.256") == False


if __name__ == "__main__":
    main()