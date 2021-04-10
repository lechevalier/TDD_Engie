from itertools import compress, cycle, zip_longest
from pathlib import Path
from typing import Iterator, Sequence, NewType, Type, Iterable

AsciiChar = list[str]
AsciiEntry = list[AsciiChar]


class OCR:

    def __init__(self, characters: str, ascii_repr: str):
        ascii_lines = ascii_repr.splitlines()
        self.height = len(ascii_lines)
        self.width, mod = divmod(len(ascii_lines[0]), len(characters))
        assert not mod
        self.reprs = dict(zip(self.split_entry(ascii_lines), characters))

    def split_entry(self, entry: Sequence[str]) -> Iterator[tuple[tuple[str], ...]]:
        print(entry)
        return zip(*[zip_longest(*entry, fillvalue=' ')] * self.width)

    def split_text(self, text: Iterable[str]) -> Iterator[tuple[str, ...]]:
        return zip(*[compress(text, cycle([1] * self.height + [0]))] * self.height)

    def read_file(self, path: Path) -> list[str]:
        with path.open('r') as f:
            return [''.join(self.reprs[digit] for digit in self.split_entry(entry))
                    for entry in self.split_text(f)]


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
