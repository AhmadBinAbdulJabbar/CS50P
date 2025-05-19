from bank import value

def test_Hello():
    assert value("Hello") == 0
    assert value("hello, Ahmad") == 0

def test_Whats():
    assert value("What's up") == 100
    assert value("Assalmu Alaikum") == 100

def test_h():
    assert value("hi") == 20
    assert value("hey") == 20
