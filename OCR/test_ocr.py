from itertools import product, zip_longest
from pathlib import Path
from typing import Iterator


class OCR:

    def __init__(self, characters: str, ascii_repr: str, tolerance: int = 0):
        ascii_lines = ascii_repr.splitlines() + ['']
        self.height = len(ascii_lines)
        self.width, mod = divmod(len(ascii_lines[0]), len(characters))
        self.tolerance = tolerance
        assert not mod and self.tolerance >= 0
        self.reprs = dict(zip(map(self.to_index, self.split_entry(ascii_lines)), characters))
        self.candidates = {n: c for n in range(1 << self.width * (self.height - 1)) if (c := self.digit_candidates(n))}
        print(self.candidates)

    def to_index(self, digit: tuple[tuple[str]]) -> int:
        return int(bytes(48 + (char == ' ') for row in digit for char in row), 2)

    def split_entry(self, entry: tuple[str]) -> Iterator[tuple[tuple[str]]]:
        assert len(entry) == self.height and not entry[-1].rstrip()
        return zip(*[zip_longest(*entry[:-1], fillvalue=' ')] * self.width)

    def split_text(self, text: str) -> Iterator[tuple[str]]:
        lines = text.replace('\n', ' ' * (self.width - 1) + '\n').splitlines() + ['']
        return zip(*[iter(lines)] * self.height)

    def read_entry(self, entry: tuple[str]) -> list[int]:
        return [self.to_index(digit) for digit in self.split_entry(entry)]

    def get_repr(self, entry: list[int]) -> str:
        return ''.join(self.reprs.get(idx, '?') for idx in entry)

    def read_file(self, path: Path) -> list[list[int]]:
        return [self.read_entry(entry) for entry in self.split_text(path.read_text())]

    def to_text(self, entries: list[list[int]]):
        return [self.get_repr(entry) for entry in entries]

    def checksum(self, account: str):
        return account.isdigit() and \
               sum(idx * int(digit) for idx, digit in enumerate(reversed(account), 1)) % 11 == 0

    def status(self, account: str) -> str:
        return 'ILL' if '?' in account else '' if self.checksum(account) else 'ERR'

    def status_with_correction(self, account: str, candidates: list[str]) -> str:
        return 'ILL' if not candidates else candidates.pop() if len(candidates) == 1 else f'{account} AMB'

    def validate_file(self, source: Path, target: Path):
        lines = [f'{account} {self.status(account)}'.rstrip() for account in map(self.get_repr, self.read_file(source))]
        target.write_text('\n'.join(lines))
        return target

    def hamming_distance(self, idx0: int, idx1: int):
        return bin(idx0 ^ idx1).count('1')

    def digit_candidates(self, target: int) -> list[str]:
        candidates = []
        for idx, digit in self.reprs.items():
            if 0 < self.hamming_distance(target, idx) <= self.tolerance:
                candidates.append(digit)
        return candidates

    def account_correction(self, idxs: list[int]) -> list[str]:
        entry_repr = self.get_repr(idxs)
        if self.checksum(entry_repr):
            return [entry_repr]
        return [corrected for idx, scanned in enumerate(idxs) for digit in self.candidates.get(scanned, [])
                if self.checksum(corrected := entry_repr[:idx] + digit + entry_repr[idx+1:])]

    def validate_file_with_correction(self, source: Path, target: Path):
        lines = [f'{self.status_with_correction(self.get_repr(account), self.account_correction(account))}'.rstrip()
                 for account in self.read_file(source)]
        target.write_text('\n'.join(lines))
        return target


class TestOCR:
    def setup_class(cls):
        ascii_digits = '''\
 _     _  _     _  _  _  _  _ 
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|
'''
        cls.digit_ocr = OCR('0123456789', ascii_digits, 1)

    def test_use_case_1(self):
        assert self.digit_ocr.to_text(self.digit_ocr.read_file(Path('use_case_1.txt'))) == [
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

    def test_use_case_4(self, tmp_path):
        assert self.digit_ocr.validate_file_with_correction(Path('use_case_4.txt'),
                                            tmp_path / 'results.txt').read_text().splitlines() == [
            "711111111",
            "777777177",
            "200800000",
            "333393333",
            "888888888 AMB",  # ['888886888', '888888880', '888888988']
            "555555555 AMB",  # ['555655555', '559555555']
            "666666666 AMB",  # ['666566666', '686666666']
            "999999999 AMB",  # ['899999999', '993999999', '999959999']
            "490067715 AMB",  # ['490067115', '490067719', '490867715']
            "123456789",
            "000000051",
            "490867715",
        ]
