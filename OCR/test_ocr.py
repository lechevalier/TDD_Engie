from itertools import compress, cycle, zip_longest
from pathlib import Path
from typing import Iterator, Sequence, NewType, Type, Iterable

AsciiChar = str
AsciiEntry = Iterable[AsciiChar]
AsciiText = Iterable[AsciiEntry]


class OCR:

    def __init__(self, characters: str, ascii_repr: str):
        ascii_lines = ascii_repr.splitlines()
        self.height = len(ascii_lines)
        self.width, mod = divmod(len(ascii_lines[0]), len(characters))
        assert not mod
        self.reprs = dict(zip(self.from_entry(ascii_lines), characters))
        print(self.reprs)

    def from_char(self, columns: Sequence[str]) -> AsciiChar:
        return ''.join(map(''.join, columns))

    def to_char(self, char: AsciiChar) -> str:
        return self.reprs[char]

    def from_entry(self, rows: Sequence[str]) -> AsciiEntry:
        return map(self.from_char, zip(*[zip_longest(*rows, fillvalue=' ')] * self.width))

    def to_entry(self, entry: AsciiEntry) -> str:
        return ''.join(map(self.to_char, entry))

    def from_text(self, rows: Iterable[str]) -> AsciiText:
        return map(self.from_entry, zip(*[compress(rows, cycle([1] * self.height + [0]))] * self.height))

    def to_text(self, text: AsciiText) -> Iterable[str]:
        return map(self.to_entry, text)

    def from_file(self, path: Path) -> AsciiText:
        with path.open('r') as f:
            yield from self.from_text(line.rstrip('\r\n') for line in f)

    def to_file(self, path: Path, content: AsciiText):
        with path.open('w') as f:
            for line in self.to_text(content):
                f.write(line)
        return path


class TestOCR:
    def setup_class(cls):
        ascii_digits = '''\
 _     _  _     _  _  _  _  _ 
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|
'''
        cls.digit_ocr = OCR('0123456789', ascii_digits)

    def test_use_case_1(self):
        assert list(self.digit_ocr.to_text(
            self.digit_ocr.from_file(Path('use_case_1.txt'))
        )) == [
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
