import babysitter as bs

sitter = bs.Babysitter()


def test_convert_time_5():
    assert sitter.convertTime(5) == 0

def test_convert_time_4():
    assert sitter.convertTime(4) == 11

def test_convert_time_12():
    assert sitter.convertTime(12) == 7



def test_validate_times_start_before_5():
    assert sitter.validateTimes(4,1,9) == False

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

def test_regular_hours_full_time():
    assert sitter.calculateRegularHours(5,4,12) == 7

def test_regular_hours_1_hour():
    assert sitter.calculateRegularHours(8,12,9) == 1

def test_regular_hours_zero():
    assert sitter.calculateRegularHours(11,2,11) == 0

def test_regular_hours_start_midnight():
    assert sitter.calculateRegularHours(12,3,1) == 0

def test_bedtime_hours_2_and_10():
    assert (sitter.calculateBedtimeHours(2,10) == 2)

def test_bedtime_hours_12_and_11():
    assert (sitter.calculateBedtimeHours(12,11) == 1) #bedtime is 11

def test_bedtime_hours_0():
    assert (sitter.calculateBedtimeHours(8,8) == 0) #bedtime is same as end

def test_bedtime_hours_bed_after_end():
    assert (sitter.calculateBedtimeHours(10,12) == 0) #bedtime is after end
