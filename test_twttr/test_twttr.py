from twttr import shorten


def test_UpLw():
    assert shorten("twitter") == "twttr"
    assert shorten("Police") == "Plc"
    assert shorten("GOoGLE") == "GGL"
    assert shorten("Yahoo") == "Yh"


def test_number():
    assert shorten("1234") == "1234"
    assert shorten("5.23") == "5.23"
    assert shorten("7/97.5") == "7/97.5"


def test_punctuation():
    assert shorten("!;,:?()") == "!;,:?()"
