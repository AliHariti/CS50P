import pytest
from jar import Jar

def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()


def  test_init():
    with pytest.raises(ValueError):
        jar = Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(13)


def test_withdraw():
    jar = Jar()
    jar.deposit(7)
    jar.withdraw(5)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(13)

if __name__ == "__main__":
    main()