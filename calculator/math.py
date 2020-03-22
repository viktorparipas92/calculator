from functools import lru_cache


def gen_to_func(gen_, n):
    """Returns the n-th item of generator function gen_"""
    gen = gen_()
    for i in range(n):
        next(gen)
    return next(gen)


def fibonacci(n):
    """Returns the n-th number of the Fibonacci series for a non-negative integer"""
    def fibo_gen():
        """Generator function for the Fibonacci series"""
        a, b = 1, 1
        while True:
            yield a
            a, b = b, a + b

    return gen_to_func(fibo_gen, n)


def test_fibonacci():
    assert(fibonacci(0) == 1)
    assert(fibonacci(1) == 1)
    assert(fibonacci(5) == 8)
    assert(fibonacci(9) + fibonacci(10) == fibonacci(11))


def factorial(n):
    """Returns the factorial (n!) of a non-negative integer"""
    def fact_gen():
        """Generator function for the factorial sequence"""
        a, b = 1, 1
        while True:
            yield a
            a, b = a*b, b+1

    return gen_to_func(fact_gen, n)


def test_factorial():
    assert(factorial(0) == 1)
    assert(factorial(1) == 1)
    assert(factorial(5) == 120)
    assert(factorial(9) * 10 == factorial(10))

@lru_cache(None)
def ackermann(m, n):
    """Returns the value of the Ackermann function with non-negative integer parameters m, n"""
    if m == 0:
        result = n + 1
    elif n == 0:
        result = ackermann(m-1, 1)
    else:
        result = ackermann(m-1, ackermann(m, n-1))

    return result


def test_ackermann():
    assert(ackermann(0, 10) == 11)
    assert(ackermann(2, 0) == 5)
    assert(ackermann(3, 0) == ackermann(2, 1))
    assert(ackermann(2, 1) == ackermann(1, ackermann(2, 0)))



