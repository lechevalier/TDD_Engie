import unittest


class FooBarQix:
    @staticmethod
    def generate(number: int) -> str:
        return str(number)


class FooBarQixTest(unittest.TestCase):
    def test_should_return_number_representation_when_number_is_regular(self):
        actual = FooBarQix.generate(1)
        self.assertEqual("1", actual)


if __name__ == '__main__':
    unittest.main()
