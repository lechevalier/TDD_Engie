import pytest

from itertools import cycle
from math import sqrt


class PrimeFactors:
    @classmethod
    def generate(cls, number):
        def _test_divisor(divisor):
            nonlocal number
            while number % divisor == 0:
                primes.append(divisor)
                number //= divisor

        primes = []
        pre_test = {
            2: (2,),  # Scan ratio: 1/2 = 0.5
            3: (4, 2),  # Scan ratio: 1/3 = 0.333
            5: (6, 4, 2, 4, 2, 4, 6, 2),  # Scan ratio: 4 / 15 = 0.2666
        }

        i, gaps = 1, (1,)
        for prime, gaps in pre_test.items():
            _test_divisor(prime)

        deltas = cycle(gaps)
        while i <= sqrt(number):
            i += next(deltas)
            _test_divisor(i)

        if number > 1:
            primes.append(number)

        return primes


class TestPrimeFactors:
    def test_generate_prime_factors_of_2(self):
        assert PrimeFactors.generate(2) == [2]

    def test_generate_prime_factors_of_3(self):
        assert PrimeFactors.generate(3) == [3]

    def test_generate_prime_factors_of_4(self):
        assert PrimeFactors.generate(4) == [2, 2]

    def test_generate_prime_factors_of_6(self):
        assert PrimeFactors.generate(6) == [2, 3]

    def test_generate_prime_factors_of_8(self):
        assert PrimeFactors.generate(8) == [2, 2, 2]

    def test_generate_prime_factors_of_9(self):
        assert PrimeFactors.generate(9) == [3, 3]

    def test_generate_prime_factors_of_10(self):
        assert PrimeFactors.generate(10) == [2, 5]

    def test_generate_prime_factors_of_12(self):
        assert PrimeFactors.generate(12) == [2, 2, 3]

    def test_generate_prime_factors_of_mersenne_prime(self):
        assert PrimeFactors.generate(2 ** 31 - 1) == [2 ** 31 - 1]

    def test_generate_prime_factors_of_false_mersenne_prime(self):
        assert PrimeFactors.generate(2 ** 42 - 1) == [3, 3, 7, 7, 43, 127, 337, 5419]

    def test_generate_prime_factors_of_false_mersenne_prime_with_big_factors(self):
        assert PrimeFactors.generate(2 ** 59 - 1) == [179951, 3203431780337]

    @pytest.mark.skip
    def test_generate_prime_factors_of_false_big_mersenne_prime(self):
        assert PrimeFactors.generate(2 ** 62 - 1) == [3, 715827883, 2147483647]

