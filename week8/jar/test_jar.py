import pytest
from week8.jar.jar import Jar

def test__init__():
    jar = Jar()

def test_str():
    jar = Jar()
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(4)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.deposit(30)

def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    jar.withdraw(4)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.withdraw(30)


