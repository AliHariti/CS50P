from seasons import life_in_minutes
import pytest

def main():
    test_result()
    test_error()


def test_result():
    assert life_in_minutes(1911, 12, 25) == "Fifty-eight million, four hundred sixty-two thousand, five hundred sixty minutes"
    assert life_in_minutes(2004, 7, 8) == "Nine million, seven hundred ninety-two thousand minutes"


def test_error():
    with pytest.raises(SystemExit):
        assert life_in_minutes(25, 10, 2000)
        assert life_in_minutes(2022, 18, 12)
        assert life_in_minutes(2022, 12, 35)

if __name__ == "__main__":
    main()

