from working import convert
import pytest


def main():
    test_wrongFormat()
    test_time()
    test_wrongHour()
    test_wrongMinute()


def test_wrongFormat():
    with pytest.raises(ValueError):
        convert('8 AM - 11 AM')


def test_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("09:00 AM to 05:30 PM") == "09:00 to 17:30"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"


def test_wrongHour():
    with pytest.raises(ValueError):
        convert('15 AM to 20 PM')


def test_wrongMinute():
    with pytest.raises(ValueError):
        convert('10:62 AM to 20:62 PM')
