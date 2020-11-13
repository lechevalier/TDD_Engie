import pytest


class StringCalculator:
    @classmethod
    def add(cls, string_number: str):
        if string_number:
            return int(string_number)
        return 0


class TestStringCalculator:
    def test_should_return_zero_when_string_is_empty(self):
        assert StringCalculator.add("") == 0

    def test_should_return_number_when_string_is_a_single_number(self):
        assert StringCalculator.add("1") == 1
