from plates import is_valid


def test_start():
    assert is_valid("CS50") == True
    assert is_valid("C50") == False


def test_len():
    assert is_valid("AAA222") == True
    assert is_valid("AAAA222") == False
    assert is_valid("ab") == True
    assert is_valid("a") == False


def test_midnum():
    assert is_valid("50CS") == False
    assert is_valid("CS50P") == False
    assert is_valid("AA20") == True
    assert is_valid("AAA22A") == False


def test_firstnum():
    assert is_valid("CSA50") == True
    assert is_valid("CSA05") == False


def test_ponctuation():
    assert is_valid("CS 50") == False
    assert is_valid("CS.50") == False
