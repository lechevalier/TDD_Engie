

import pytest

from WordWrapper.word_wrapper import Wrapper


class TestWordWrapper:
    def test_should_return_identical_string_when_column_number_is_larger(self):
        assert Wrapper.wrap("a", 2) == "a"

    def test_should_break_at_boundaries_when_column_number_match_boundary(self):
        assert Wrapper.wrap("ab cd", 2) == "ab\ncd"

    def test_should_break_at_boundaries_when_column_number_is_greater_than_boundary(self):
        assert Wrapper.wrap("ab cd", 3) == "ab\ncd"

    def test_should_break_words_at_column_number_when_column_number_is_smaller_than_string(self):
        assert Wrapper.wrap("abcd", 2) == "ab\ncd"

    def test_should_break_at_boundary_twice_when_column_number_is_greater_than_boundary(self):
        assert Wrapper.wrap("ab cd ef", 2) == "ab\ncd\nef"

    def test_should_break_at_boundary_a_thousand_times_when_column_number_is_greater_than_boundary(self):
        assert Wrapper.wrap("ab " * 1001, 2) == "ab\n" * 1001
