import pytest


class StringCalculator:
    @classmethod
    def add(cls, string_number: str):
        if not string_number:
            return 0

        delimiter = ","
        if string_number.startswith("//"):
            delimiter = string_number[2]
            string_number = string_number[4:]

        string_number = string_number.replace("\n", ",")
        str_numbers = string_number.split(delimiter)
        numbers = list(map(int, str_numbers))

        negatives = [number for number in numbers if number < 0]
        if negatives:
            raise ValueError(f"Negatives not allowed: {','.join(map(str, negatives))}")

        return sum(num for num in numbers if num <= 1000)


class TestStringCalculator:
    def test_should_return_zero_when_string_is_empty(self):
        assert StringCalculator.add("") == 0

    def test_should_return_number_when_string_is_a_single_number(self):
        assert StringCalculator.add("1") == 1

    def test_should_return_sum_of_numbers_when_string_is_composed_of_several_number_representation(self):
        assert StringCalculator.add("1,2,3") == 6

    def test_should_return_sum_of_numbers_when_separated_by_comma_and_new_line(self):
        assert StringCalculator.add("1\n2,3") == 6

    def test_should_return_sum_of_number_in_string_separated_by_given_delimiter(self):
        assert StringCalculator.add("//;\n1;2") == 3

    def test_should_raise_an_exception_when_negative_numbers_are_present(self):
        with pytest.raises(ValueError):
            StringCalculator.add("-1,2")

    def test_should_ignore_number_bigger_than_1000(self):
        assert StringCalculator.add("1001,2") == 2
