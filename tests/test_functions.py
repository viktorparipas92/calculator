from calculator.functions import fibonacci, factorial, ackermann


def test_fibonacci():
    assert(fibonacci(0) == 1)
    assert(fibonacci(1) == 1)
    assert(fibonacci(5) == 8)
    assert(fibonacci(9) + fibonacci(10) == fibonacci(11))


def test_factorial():
    assert(factorial(0) == 1)
    assert(factorial(1) == 1)
    assert(factorial(5) == 120)
    assert(factorial(9) * 10 == factorial(10))


def test_ackermann():
    assert(ackermann(0, 10) == 11)
    assert(ackermann(2, 0) == 3)
    assert(ackermann(3, 0) == ackermann(2, 1))
    assert(ackermann(2, 1) == ackermann(1, ackermann(2, 0)))