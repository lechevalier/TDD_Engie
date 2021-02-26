import math


class PrimeFactors(object):
    @classmethod
    def is_prime(cls, number):
        if number < 2:
            return False

        if number == 2:
            return True

        return all(number % i for i in range(2, math.floor(math.sqrt(number)) + 1))

    @classmethod
    def generate(cls, number):
        primes = []
        for i in range(2, math.floor(math.sqrt(number)) + 1):
            if cls.is_prime(i):
                while number % i == 0:
                    primes.append(i)
                    number = number // i

        if cls.is_prime(number):
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

