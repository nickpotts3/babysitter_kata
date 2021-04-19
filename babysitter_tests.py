import babysitter as bs

sitter = bs.Babysitter()


def test_convert_time_5():
    assert sitter.convertTime(5) == 0

def test_convert_time_4():
    assert sitter.convertTime(4) == 11

def test_convert_time_12():
    assert sitter.convertTime(12) == 7

def test_validate_times_start_before_5():
    assert sitter.validateTimes(4,1,9) == False # start at 5

def test_validate_times_start_after_end():
    assert sitter.validateTimes(7,5,10) == False

def test_validate_times_5_to_4():
    assert sitter.validateTimes(5,4,12) == True

def test_validate_times_bednight_is_12():
    assert sitter.validateTimes(5,2,12) == True

def test_validate_times_start_equals_bedtime():
    assert sitter.validateTimes(8,12,8) == True

def test_validate_times_neg_start():
    assert sitter.validateTimes(-5,12,10) == False

def test_validate_times_neg_end():
    assert sitter.validateTimes(5,-12,10) == False

def test_validate_times_neg_bedtime():
    assert sitter.validateTimes(5,12,-10) == False

