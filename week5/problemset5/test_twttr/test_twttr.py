from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("apple") == "ppl"

def test_case_sensitivity():
    assert shorten("TwItTeR") == "TwtTR"
    assert shorten("AeIOu") == ""

def test_no_vowel():
    assert shorten("bcdfg") == "bcdfg"

def test_only_vowels():
    assert shorten("aeiouAEIOU") == ""

def test_numbers():
    assert shorten("h3ll0") == "h3ll0"
    assert shorten("12345") == "12345"

def test_special_characters():
    assert shorten("h@ppy!") == "h@ppy!"
    assert shorten("hello, world!") == "hll, wrld!"

def test_mixed():
    assert shorten("CS50 is Awesome!") == "CS50 s wsm!"
