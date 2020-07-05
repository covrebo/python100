from fizz_buzz import fizzbuzz

def test_fizzbuzz():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(3) == '3 fizz'
    assert fizzbuzz(5) == '5 buzz'
    assert fizzbuzz(15) == '15 fizz buzz'