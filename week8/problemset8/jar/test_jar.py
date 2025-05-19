from jar import Jar
import pytest

def test_init():
    jar = Jar(5)
    assert jar.capacity == 5

    with pytest.raises(ValueError):
        jar1 = Jar(-2)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(3)
    assert jar.size == 8

    with pytest.raises(ValueError):
        jar.deposit(-2)

    with pytest.raises(ValueError):
        jar.deposit(11)


def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5

    jar.withdraw(3)
    assert jar.size == 2


    with pytest.raises(ValueError):
        jar.withdraw(10)

    with pytest.raises(ValueError):
        jar.withdraw(-2)

