from bank import value


def test_hello():
    assert value("hello sir") == 0
    assert value("Hello") == 0
    assert value("good morning") == 100


def test_h():
    assert value("hey") == 20
    assert value("hola") == 20


def test_number():
    assert value("1") == 100
