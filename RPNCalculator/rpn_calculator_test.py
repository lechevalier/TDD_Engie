import pytest

from RPNCalculator.rpn_calculator import RpnCalculator


class TestRpnCalculator:
    def test_should_return_digit_when_input_is_a_digit(self):
        assert RpnCalculator("1").eval("1") == "1"

    def test_should_return_in_two_lines_when_enter_after_two_numbers(self):
        assert RpnCalculator("1 5").eval("1 5") == "1\n5"

    def test_should_return_sum_when_operator_add_after_two_numbers(self):
        assert RpnCalculator("1 5 +").eval("1 5 +") == "6"

    def test_should_return_product_when_operator_is_multiplier_after_two_numbers(self):
        assert RpnCalculator("2 5 *").eval("2 5 *") == "10"

    def test_should_return_substraction_when_operator_is_sub_after_two_numbers(self):
        assert RpnCalculator("10 5 -").eval("10 5 -") == "5"

    def test_should_return_division_when_operator_is_div_after_two_numbers(self):
        assert RpnCalculator("10 5 /").eval("10 5 /") == "2.0"

    def test_should_return_result_when_multiple_operators(self):
        assert RpnCalculator("4 2 + 3 -").eval("4 2 + 3 -") == "3"

    def test_should_return_result_when_multiple_operators_with_priority(self):
        assert RpnCalculator("3 5 8 * 7 + *").eval("3 5 8 * 7 + *") == "141"
