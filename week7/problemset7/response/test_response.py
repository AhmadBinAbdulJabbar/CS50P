from response import check_email

def test_check_email():
    assert check_email("ahmadbinabduljabbar@gmail.com") == "Valid"
    assert check_email("ahmad@gmail.com") == "Valid"
    assert check_email("malan@harvard.edu") == "Valid"

def test_check_email_invalid():
    assert check_email("ahmad@@gmail.com") == "Invalid"
    assert check_email("ahmad@@gmailcom") == "Invalid"
    assert check_email("malan@@@harvard.edu") == "Invalid"
    assert check_email("malan@.harvard.edu") == "Invalid"
