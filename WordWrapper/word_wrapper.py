class Wrapper:
    @staticmethod
    def wrap(strng: str, column_number: int) -> str:
        return strng


class TestWordWrapper:
    def test_should_return_identical_string_when_column_number_is_larger(self):
        assert Wrapper.wrap("a", 2) == "a"
