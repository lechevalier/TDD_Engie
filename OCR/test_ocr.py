from itertools import zip_longest
from pathlib import Path
from typing import Iterator


class OCR:

    def __init__(self, characters: str, ascii_repr: str):
        ascii_lines = ascii_repr.splitlines() + ['']
        self.height = len(ascii_lines)
        self.width, mod = divmod(len(ascii_lines[0]), len(characters))
        assert not mod
        self.reprs = dict(zip(self.split_entry(ascii_lines), characters))

    def split_entry(self, entry: tuple[str]) -> Iterator[tuple[tuple[str]]]:
        assert len(entry) == self.height and not entry[-1].rstrip()
        return zip(*[zip_longest(*entry[:-1], fillvalue=' ')] * self.width)

    def split_text(self, text: str) -> Iterator[tuple[str]]:
        lines = text.replace('\n', ' ' * (self.width - 1) + '\n').splitlines() + ['']
        return zip(*[iter(lines)] * self.height)

    def read_file(self, path: Path) -> list[str]:
        return [''.join(self.reprs[digit] for digit in self.split_entry(entry))
                for entry in self.split_text(path.read_text())]


class TestOCR:
    def setup_class(cls):
        ascii_digits = '''\
 _     _  _     _  _  _  _  _ 
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|
'''
        cls.digit_ocr = OCR('0123456789', ascii_digits)

    def test_use_case_1(self):
        assert self.digit_ocr.read_file(Path('use_case_1.txt')) == [
            '000000000',
            '111111111',
            '222222222',
            '333333333',
            '444444444',
            '555555555',
            '666666666',
            '777777777',
            '888888888',
            '999999999',
            '123456789',
        ]
