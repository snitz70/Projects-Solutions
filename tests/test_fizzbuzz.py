import fizzbuzz


def test_multiple_of_three():
    assert fizzbuzz.multiple_of_three(3) == 'fizz'


def test_not_multiple_of_three():
    assert fizzbuzz.multiple_of_three(4) == 4


def test_multiple_of_five():
    assert fizzbuzz.multiple_of_five(5) == 'buzz'


def test_not_multiple_of_five():
    assert fizzbuzz.multiple_of_five(6) == 6


def test_multiple_of_15():
    assert fizzbuzz.multiple_of_fifteen(30) == 'fizzbuzz'


def test_combine


def test_fizzbuzz():
    assert fizzbuzz.fizzbuzz(10) == [1,2,'fizz',4,'buzz','fizz',7,8,'fizz','buzz']

