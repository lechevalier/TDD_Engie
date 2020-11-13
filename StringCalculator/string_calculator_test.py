import pytest


class StringCalculator:
    @classmethod
    def add(cls, s: str):
        return 0


class TestStringCalculator:
    def test_should_return_zero_when_string_is_empty(self):
        assert StringCalculator.add("") == 0
