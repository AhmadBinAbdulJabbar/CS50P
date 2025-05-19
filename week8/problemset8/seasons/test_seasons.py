from seasons import get_minutes_since

def test_one_year():
    assert get_minutes_since("2024-04-13") in ["Five hundred twenty-five thousand, six hundred minutes", "Five hundred twenty-seven thousand forty minutes"]
    assert get_minutes_since("2023-04-13") in ["One million, fifty-one thousand, two hundred minutes", "One million, fifty-two thousand, six hundred forty minutes"]

def test_invalid_format():
    try:
        get_minutes_since("13-04-2024")
    except SystemExit:
        assert True
