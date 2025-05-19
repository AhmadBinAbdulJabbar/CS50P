import pytest

from fuel import convert, gauge


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(25) == "25%"
    assert gauge(70) == "70%"


def test_convert():
    assert convert("1/2") == 50
    assert convert("1/100") == 1
    assert convert("99/100") == 99

def test_convert_raises():
    with pytest.raises(ValueError):
        convert("10/9")
        convert("5/2")

    with pytest.raises(ZeroDivisionError):
        convert("1/0")
        convert("10/0")

