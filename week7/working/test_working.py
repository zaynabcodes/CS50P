import pytest
from working import convert

def test_invalid():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")
    with pytest.raises(ValueError):
        convert("12:60 AM to 13:00 PM")

def test_valid():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"