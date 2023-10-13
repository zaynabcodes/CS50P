from twttr import shorten

def test_shorten():
  assert shorten("hello") == "hll"
  assert shorten("Goodbye") == "Gdby"
  assert shorten("What's your name?") == "Wht's yr nm?"

def test_upper():
  assert shorten("hEllO") == "hll"
  assert shorten("GOOdbyE") == "Gdby"
  assert shorten("WhAt's yOUr nAmE?") == "Wht's yr nm?"

def test_numbers():
  assert shorten("I love 1") == " lv 1"
