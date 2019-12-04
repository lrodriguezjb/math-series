from series import fibonacci, lucas, sum_func


def test_one():
    expected = 55
    actual = fibonacci(10)
    assert actual == expected


def test_two():
    expected = 3
    actual = fibonacci(4)
    assert actual == expected


def test_three():
    expected = 8
    actual = fibonacci(6)
    assert actual == expected


# Lucas
# ------------------------------------------------------

def test_four():
    expected = 76
    actual = lucas(10)
    assert actual == expected


def test_five():
    expected = 4
    actual = lucas(4)
    assert actual == expected


def test_six():
    expected = 11
    actual = lucas(6)
    assert actual == expected


# Sum Function
# ------------------------------------------------------

def test_seven():
    expected = 18
    actual = sum_func(7, 1, 2)
    assert actual == expected


def test_eight():
    expected = 26
    actual = sum_func(6, 4, 2)
    assert actual == expected


def test_nine():
    expected = 31
    actual = sum_func(6, 5, 2)
    assert actual == expected
