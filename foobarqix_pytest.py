class FooBarQix:
    @staticmethod
    def generate(number: int) -> str:
        return str(number)


class TestFooBarQix:
    def test_should_return_number_representation_when_number_is_regular(self):
        assert FooBarQix.generate(1) == "1"
