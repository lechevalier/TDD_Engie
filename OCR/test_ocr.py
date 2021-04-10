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
        return [''.join(self.reprs.get(digit, '?') for digit in self.split_entry(entry))
                for entry in self.split_text(path.read_text())]

    def checksum(self, account: str):
        return sum(idx * int(digit) for idx, digit in enumerate(reversed(account), 1)) % 11 == 0

    def status(self, account: str) -> str:
        return 'ILL' if '?' in account else '' if self.checksum(account) else 'ERR'

    def validate_file(self, source: Path, target: Path):
        lines = [f'{account} {self.status(account)}'.rstrip() for account in self.read_file(source)]
        target.write_text('\n'.join(lines))
        return target


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

    def test_use_case_2(self):
        tests = [
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
        assert list(map(self.digit_ocr.checksum, tests)) == [
            True,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            True,
        ]

    def test_use_case_3(self, tmp_path):
        assert self.digit_ocr.validate_file(Path('use_case_3.txt'),
                                            tmp_path / 'results.txt').read_text().splitlines() == [
                   '000000051',
                   '490067715 ERR',
                   '49006771? ILL',
                   '1234?678? ILL',
               ]
