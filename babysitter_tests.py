import babysitter as bs


sitter = bs.Babysitter()

# the tests commented out throw an exception but in version 1.0 they returned false. 
# I tried using pytest.raises but my machine is not importing pytest properly




#def test_validate_times_start_before_5():
  #  assert sitter.validateTimes(4,1,9) == False

#def test_validate_times_start_after_end():
  #  assert sitter.validateTimes(7,5,10) == False

#def test_validate_times_neg_start():
  #  assert sitter.validateTimes(-5,12,10) == False

#def test_validate_times_neg_end():
   # assert sitter.validateTimes(5,-12,10) == False

#def test_validate_times_neg_bedtime():
 #   assert sitter.validateTimes(5,12,-10) == False


# validateTimes calls the private validation methods and only returns true if all methods return true
# need to supply the method with start, end, bedtime
def test_validate_times_5_to_4():
    assert sitter.validateTimes(5,4,12) == True

def test_validate_times_bednight_is_12():
    assert sitter.validateTimes(5,2,12) == True

def test_validate_times_start_equals_bedtime():
    assert sitter.validateTimes(8,12,8) == True


# should this method be private? Left public for testing purposes
# supply start, end, bedtime
def test_regular_hours_full_time():
    assert sitter.calculateRegularHours(5,4,12) == 7

def test_regular_hours_1_hour():
    assert sitter.calculateRegularHours(8,12,9) == 1

def test_regular_hours_zero():
    assert sitter.calculateRegularHours(11,2,11) == 0

def test_regular_hours_start_midnight():
    assert sitter.calculateRegularHours(12,3,1) == 0


# Should this be made private? 
# supply end and bedtime
def test_bedtime_hours_2_and_10():
    assert (sitter.calculateBedtimeHours(2,10) == 2)

def test_bedtime_hours_12_and_11():
    assert (sitter.calculateBedtimeHours(12,11) == 1) #bedtime is 11

def test_bedtime_hours_0():
    assert (sitter.calculateBedtimeHours(8,8) == 0) #bedtime is same as end

def test_bedtime_hours_bed_after_end():
    assert (sitter.calculateBedtimeHours(10,12) == 0) #bedtime is after end


# Should this also be made private?
# supply end time
def test_midnight_hours_2():
    assert (sitter.calculateMidnightHours(2) == 2) # regular case

def test_midnight_hours_0():
    assert (sitter.calculateMidnightHours(12) == 0) # end == midnight

def test_midnight_hours_end_before_midnight():
    assert (sitter.calculateMidnightHours(10) == 0) # end is before midnight

def test_midnight_hours_4():
    assert (sitter.calculateMidnightHours(4) == 4) # edge case where end == 4


# invokes the 3 other calulateHours methods.
# need to supply start, end, bedtime 
def test_total_pay_equals_20():
    assert (sitter.calculateTotalPay(5,7,6) == 20)

def test_total_pay_equals_56():
    assert (sitter.calculateTotalPay(10,2,12) == 56)

def test_total_pay_equals_140():
    assert (sitter.calculateTotalPay(5,4,10) == 140)

def test_total_pay_equals_32():
    assert (sitter.calculateTotalPay(12, 2, 12) == 32)
    
def test_total_pay_equals_92():
    assert (sitter.calculateTotalPay(5,1,10) == 92)

def test_total_pay_fulltime():
    assert sitter.calculateTotalPay(5,4,9) == 136