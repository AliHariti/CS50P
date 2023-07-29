from um import count


def main():
    test_count()


def test_count():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("Hello, um, world") == 1
    assert count("drums?") == 0
    assert count("yumy") == 0
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2
