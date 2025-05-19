from plates import is_valid

def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("AAA222") == True

def test_invalid():
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False

def test_only_numbers():
    assert is_valid("50") == False
    assert is_valid("05") == False

def test_only_alpha():
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False

def test_no_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("AHMAD#123") == False

