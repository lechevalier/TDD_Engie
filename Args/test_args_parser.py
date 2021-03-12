import pytest


class ArgParser(object):
    def __init__(self, boolean_args: list = None, integer_args: list = None):
        self.boolean_args = boolean_args or []
        self.integer_args = integer_args or []

    def load(self, input: str) -> dict:
        args = {arg: False for arg in self.boolean_args}
        # ""-"l" -"d 10" -"p test"
        flags = [c.rstrip() for c in input.split("-")][1:]

        for flag in flags:
            f, *v = flag.split()
            if flag in self.boolean_args:
                args[f] = True
            elif f in self.integer_args:
                args[f] = v and int(v[0]) or 0
            else:
                raise KeyError(f"Unknown flag: {f}")

        return args


class TestArgsParser:
    def test_arg_parser_should_read_boolean_flag(self):
        assert ArgParser(["l"]).load("-l") == {"l": True}

    def test_arg_parser_should_default_boolean_to_false(self):
        assert ArgParser(["l"]).load("") == {"l": False}

    def test_arg_parser_should_ignore_non_flag(self):
        assert ArgParser(["l"]).load("l") == {"l": False}

    def test_arg_parser_should_reject_unknown_flag(self):
        with pytest.raises(KeyError):
            ArgParser(["l"]).load("-x")

    def test_arg_parser_with_multiple_flags_should_read_boolean_flag(self):
        assert ArgParser(["b", "l"]).load("-b") == {"b": True, "l": False}

    def test_arg_parser_should_read_multiple_boolean_flags(self):
        assert ArgParser(["b", "l"]).load("-b -l") == {"b": True, "l": True}

    def test_arg_parser_should_read_integer_flag(self):
        assert ArgParser(integer_args=["p"]).load("-p 0") == {"p": 0}

    def test_arg_parser_should_read_multiple_flags(self):
        assert ArgParser(["l"], ["p"]).load("-l -p 1") == {"l": True, "p": 1}
