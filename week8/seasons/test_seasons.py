# tests seasons.py

from week8.seasons.seasons import check

def test_valid():
    assert str(check("2022-10-08")) == "Five hundred twenty-five thousand, six hundred minutes"