from week7.um.um import count

def test_valid():
    assert count(" um , hello") == 1

def test_inword():
    assert count("yummy") == 0

def test_insensitive():
    assert count("Um... hello um hello this is so many um and um and um") == 5