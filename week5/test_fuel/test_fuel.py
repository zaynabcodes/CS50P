import pytest
from test_plates.fuel import convert, gauge

def test_convert():
    with pytest.raises(ValueError):
        convert("one/two")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/4") == 25

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
