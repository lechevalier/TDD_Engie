from typing import Dict, Callable, Any, Optional, List

import pytest


def bool_factory(input: Optional[str]) -> bool:
    return False if input is None else True


def int_factory(input: Optional[str]) -> int:
    if input is None:
        return 0
    if input and not input.isdigit():
        raise ValueError("Should be digits.")
    return int(input)


def str_factory(input: Optional[str]) -> str:
    return "" if input is None else input


def str_list_factory(input: Optional[str]) -> List[str]:
    return [] if input is None else list(map(str_factory, input.split(',')))


def int_list_factory(input: Optional[str]) -> List[str]:
    return [] if input is None else list(map(int_factory, input.split(',')))


class ArgParser(object):
    def __init__(self, schema: Dict[str, Callable[[Optional[str]], Any]]):
        import re
        self.flag_regex = re.compile(r'-[a-zA-Z]()?')
        self.schema = schema

    def split(self, input: str) -> List[str]:
        # ""-"l" -"p 10" -"d test"
        flag_pairs = []
        for c in input.split("-")[1:]:
            try:
                if c[0].isalpha():
                    flag_pairs.append(c.rstrip())
                else:
                    flag_pairs[-1] = flag_pairs[-1] + " -" + c.rstrip()
            except IndexError:
                raise ValueError(f"Value not allowed for a flag: {c}")
        return flag_pairs

        # return self.flag_regex.findall(input)

    def load(self, input: str) -> dict:
        # Defaulting
        args = {flag: factory(None) for flag, factory in self.schema.items()}

        flags = self.split(input)

        # Parsing
        for flag in flags:
            f, *v = flag.split()
            v = ''.join(v)
            if not f.isalpha():
                raise ValueError(f"Value not allowed for a flag: {f}")
            if f not in self.schema:
                raise KeyError(f"Unknown flag: {f}")
            args[f] = self.schema[f](v)

        return args


class TestArgsSplitter:
    def test_should_split_simple_flag(self):
        assert ArgParser({}).split("-l") == ["l"]

    def test_should_split_two_flags(self):
        assert ArgParser({}).split("-l -p") == ["l", "p"]

    def test_should_split_simple_flag_with_value(self):
        assert ArgParser({}).split("-p 100") == ["p 100"]

    def test_should_split_flag_with_negatif_value(self):
        assert ArgParser({}).split("-p -100") == ["p -100"]

    def test_shouldnt_split_flag_with_integer_value(self):
        with pytest.raises(ValueError):
            ArgParser({}).split("-1")

    def test_shouldnt_split_flag_with_boolean_flag_and_negative_number(self):
        with pytest.raises(ValueError):
            ArgParser({}).split("-l -1")


class TestArgsParser:
    def test_arg_parser_should_read_boolean_flag(self):
        assert ArgParser({"l": bool_factory}).load("-l") == {"l": True}

    def test_arg_parser_should_default_boolean_to_false(self):
        assert ArgParser({"l": bool_factory}).load("") == {"l": False}

    def test_arg_parser_should_ignore_non_flag(self):
        assert ArgParser({"l": bool_factory}).load("l") == {"l": False}

    def test_arg_parser_should_reject_unknown_flag(self):
        with pytest.raises(KeyError):
            ArgParser({"l": bool_factory}).load("-x")

    def test_arg_parser_should_reject_incorrect_flag(self):
        with pytest.raises(ValueError):
            ArgParser({"p": int_factory}).load("-1 10")

    def test_arg_parser_with_multiple_flags_should_read_boolean_flag(self):
        assert ArgParser({"b": bool_factory, "l": bool_factory}).load("-b") == {"b": True, "l": False}

    def test_arg_parser_should_read_multiple_boolean_flags(self):
        assert ArgParser({"b": bool_factory, "l": bool_factory}).load("-b -l") == {"b": True, "l": True}

    def test_arg_parser_should_read_integer_flag(self):
        assert ArgParser({"p": int_factory}).load("-p 0") == {"p": 0}

    def test_arg_parser_should_read_negative_integer(self):
        assert ArgParser({"n": int_factory}).load("-n -10") == {"n": -10}

    def test_arg_parser_should_return_zero_when_int_flag_is_missing(self):
        assert ArgParser({"p": int_factory}).load("") == {"p": 0}

    def test_arg_parser_should_raise_value_error_for_illegal_value_with_integer_flag(self):
        with pytest.raises(ValueError):
            ArgParser({"p": int_factory}).load("-p x")

    def test_arg_parser_should_raise_value_error_for_empty_value_with_integer_flag(self):
        with pytest.raises(ValueError):
            ArgParser({"q": int_factory}).load("-q")

    def test_arg_parser_should_read_str_flag(self):
        assert ArgParser({"d": str_factory}).load("-d /usr/logs") == {"d": "/usr/logs"}

    def test_arg_parser_should_return_empty_string_when_str_flag_is_missing(self):
        assert ArgParser({"d": str_factory}).load("") == {"d": ""}

    def test_arg_parser_should_read_multiple_flags(self):
        assert ArgParser(
            {"l": bool_factory, "p": int_factory, "d": str_factory}
        ).load("-l -p 10 -d /usr/logs") == {"l": True, "p": 10, "d": "/usr/logs"}

    def test_arg_parser_should_read_str_list_flag(self):
        assert ArgParser({"g": str_list_factory}).load("-g this,is,a,list") == {"g": ["this", "is", "a", "list"]}

    def test_arg_parser_should_read_int_list_flag(self):
        assert ArgParser({"d": int_list_factory}).load("-d 1,2,3,4") == {"d": [1, 2, 3, 4]}

    def test_arg_parser_should_raise_value_error_for_illegal_value_with_integer_list_flag(self):
        with pytest.raises(ValueError):
            ArgParser({"d": int_list_factory}).load("-d a,2,3,4")
