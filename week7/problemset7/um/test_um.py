from um import count
import pytest

def test_count_small():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("yummy") == 0

def test_count_with_words():
    assert count("Hello, um, world") == 1
    assert count("um, Hello, um, world") == 2


def test_count_capital():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

