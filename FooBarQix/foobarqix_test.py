import unittest

from FooBarQix.foobarqix import FooBarQix


class FooBarQixTest(unittest.TestCase):
    def setUp(self):
        self.foo_bar_qix = FooBarQix({
            3: "Foo",
            5: "Bar",
            7: "Qix",
        })

    def test_should_return_number_representation_when_number_is_regular(self):
        self.assertEqual("1", self.foo_bar_qix.generate(1))

    def test_should_return_foo_when_number_is_divisible_by_three(self):
        self.assertEqual("Foo", self.foo_bar_qix.generate(9))

    def test_should_return_bar_when_number_is_divisible_by_five_and_contains_five(self):
        self.assertEqual("BarBar", self.foo_bar_qix.generate(5))

    def test_should_return_qix_when_number_is_divisible_by_seven_and_doesnt_contain_7(self):
        self.assertEqual("Qix", self.foo_bar_qix.generate(14))

    def test_should_return_foobar_when_number_is_divisible_by_three_and_five_and_contains_five(self):
        self.assertEqual("FooBarBar", self.foo_bar_qix.generate(15))

    def test_should_return_foo_when_number_contains_three_and_is_not_divisible_by_three(self):
        self.assertEqual("Foo", self.foo_bar_qix.generate(23))

    def test_should_return_foofoofoo_when_number_contains_three_twice_and_is_divisible_by_three(self):
        self.assertEqual("FooFooFoo", self.foo_bar_qix.generate(33))

    def test_should_return_foo_when_number_contains_five_and_is_not_divisible_by_five(self):
        self.assertEqual("Bar", self.foo_bar_qix.generate(52))

    def test_should_return_qix_when_number_is_not_divisible_by_seven_and_contains_7(self):
        self.assertEqual("Qix", self.foo_bar_qix.generate(71))

    def test_should_return_qix_when_number_is_divisible_by_seven_and_contains_7(self):
        self.assertEqual("QixQix", self.foo_bar_qix.generate(7))


if __name__ == '__main__':
    unittest.main()
