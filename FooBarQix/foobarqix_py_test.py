from FooBarQix.foobarqix import FooBarQix


class TestFooBarQix:
    def setup_method(self):
        self.foo_bar_qix = FooBarQix({
            3: "Foo",
            5: "Bar",
            7: "Qix",
        })

    def test_should_return_number_representation_when_number_is_regular(self):
        assert self.foo_bar_qix.generate(1) == "1"

    def test_should_return_foo_when_number_is_divisible_by_three(self):
        assert self.foo_bar_qix.generate(9) == "Foo"

    def test_should_return_bar_when_number_is_divisible_by_five_and_contains_five(self):
        assert self.foo_bar_qix.generate(5) == "BarBar"

    def test_should_return_qix_when_number_is_divisible_by_seven_and_doesnt_contain_7(self):
        assert self.foo_bar_qix.generate(14) == "Qix"

    def test_should_return_foobar_when_number_is_divisible_by_three_and_five_and_contains_five(self):
        assert self.foo_bar_qix.generate(15) == "FooBarBar"

    def test_should_return_foo_when_number_contains_three_and_is_not_divisible_by_three(self):
        assert self.foo_bar_qix.generate(23) == "Foo"

    def test_should_return_foofoofoo_when_number_contains_three_twice_and_is_divisible_by_three(self):
        assert self.foo_bar_qix.generate(33) == "FooFooFoo"

    def test_should_return_foo_when_number_contains_five_and_is_not_divisible_by_five(self):
        assert self.foo_bar_qix.generate(52) == "Bar"

    def test_should_return_qix_when_number_is_not_divisible_by_seven_and_contains_7(self):
        assert self.foo_bar_qix.generate(71) == "Qix"

    def test_should_return_qix_when_number_is_divisible_by_seven_and_contains_7(self):
        assert self.foo_bar_qix.generate(7) == "QixQix"
