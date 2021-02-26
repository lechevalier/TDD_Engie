class PrimeFactors(object):
    @classmethod
    def generate(cls, number):
        return [number]


class TestPrimeFactors:
    def test_generate_prime_factors_of_2(self):
        assert PrimeFactors.generate(2) == [2]

    def test_generate_prime_factors_of_3(self):
        assert PrimeFactors.generate(3) == [3]

