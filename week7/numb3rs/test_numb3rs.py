# test_numb3rs.py
from numb3rs import validate

def test_valid():
    assert validate("255.255.255.0") == True
    assert validate("127.0.0.1") == True
    assert validate("1.2.3.4") == True

def test_invalid():
    assert validate("512.512.512.512") == False
    assert validate("cat") == False
    assert validate("1.2.3") == False
    assert validate("22") == False