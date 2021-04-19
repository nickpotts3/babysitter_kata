import babysitter as bs

sitter = bs.Babysitter()


def test_convert_time_5():
    assert sitter.convertTime(5) == 0

def test_convert_time_4():
    assert sitter.convertTime(4) == 11

def test_convert_time_12():
    assert sitter.convertTime(12) == 7
