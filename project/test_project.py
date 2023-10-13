from project import start_timer, end_time, check_letter

# Test start_timer function
def test_start_timer():
    start = start_timer()
    assert isinstance(start, float)

# Test end_time function
def test_end_time():
    start = 0.0
    end = end_time(start)
    assert isinstance(end, float)

# Test if a valid letter returns true
def test_check_letter_valid():
    letter = 'p'
    assert check_letter(letter) == True

#Test if a invalid letter returns false
def test_check_letter_invalid():
    letter = '.'
    assert check_letter(letter) == False
