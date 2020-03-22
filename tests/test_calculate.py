import pytest
import re


def test_calculate(client):
    def test_get(client):
        assert client.get('/').status_code == 200

    def test_ackermann_ok(client):
        response = client.post('/', data={'formula': 'ack', 'num1': 2, 'num2': 3})
        assert response.status_code == 200
        assert b"ack(2, 3) = 9" in response.data

    def test_factorial_ok(client):
        response = client.post('/', data={'formula': 'fact', 'num1': 4})
        assert response.status_code == 200
        assert b"fact(4) = 24" in response.data

    def test_fibonacci_ok(client):
        response = client.post('/', data={'formula': 'fibo', 'num1': 4})
        assert response.status_code == 200
        assert b"fibo(4) = 5" in response.data

    def test_elapsed_time(client):
        response = client.post('/', data={'formula': 'fact', 'num1': 4})
        pattern = re.compile(br"took \d*\.\d* seconds")
        assert pattern.findall(response.data)

    # These cases cannot actually occur because of validating the input on the front-end
    # TODO: Test in Selenium
    def test_no_formula(client):
        with pytest.raises(KeyError):
            client.post('/', data={})

    def test_ackermann_raises(client):
        with pytest.raises(KeyError):
            client.post('/', data={'formula': 'ack', 'num1': 4})

    def test_factorial_raises(client):
        with pytest.raises(KeyError):
            client.post('/', data={'formula': 'fact'})

    def test_fibonacci_raises(client):
        with pytest.raises(KeyError):
            client.post('/', data={'formula': 'fibo'})

    def test_input_not_integer(client):
        with pytest.raises(ValueError):
            client.post('/', data={'formula': 'fibo', 'num1': 'four'})

    def test_ackermann_too_large(client):
        response = client.post('/', data={'formula': 'ack', 'num1': 6, 'num2': 3})
        assert b"ack(6, 3) = None" in response.data

    test_get(client)

    test_ackermann_ok(client)
    test_factorial_ok(client)
    test_fibonacci_ok(client)
    test_elapsed_time(client)

    test_no_formula(client)
    test_ackermann_raises(client)
    test_factorial_raises(client)
    test_fibonacci_raises(client)
    test_input_not_integer(client)
    test_ackermann_too_large(client)


