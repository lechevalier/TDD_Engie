from typing import List

from OCR.digit_helper import generate_ascii_patterns

ASCII_PATTERNS_ROWS = generate_ascii_patterns()


class OCR:

    def sanitize(self, input: str) -> str:
        lines = input.splitlines() + ['']
        max_length = max(map(len, lines))
        return '\n'.join(line.ljust(max_length) for line in lines)

    def print_entry(self, entry):
        for digit in entry:
            print()
            print('\n'.join(digit))
            print()

    def read(self, file_path: str) -> List[str]:
        with open(file_path) as f:
            lines = self.sanitize(f.read()).splitlines()
        # for _ in lines: print(_)
        return [self.read_entry(lines[i: i+4]) for i in range(0, len(lines), 4)]

    def read_entry(self, lines: List[str]) -> str:
        entry = [[line[i: i+3] for line in lines[:-1]] for i in range(0, len(lines[0]), 3)]
        if False:
            self.print_entry(entry)
        return ''.join(str(self.read_digit(digit)) for digit in entry)

    def read_digit(self, ascii_chars: List[str]):
        candidates = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        for i, ascii in enumerate(ascii_chars):
            candidates.intersection_update(ASCII_PATTERNS_ROWS[i][ascii])
        # print(candidates)
        if len(candidates) == 0:
            return "?"
        assert len(candidates) == 1
        return candidates.pop()

    # def checksum_(self, number_str: str) -> bool:
    #     return len(number_str) == 9 and number_str.isdigit and \
    #         sum(idx * int(digit) for idx, digit in enumerate(reversed(number_str), 1)) % 11 == 0

    def checksum(self, number_str: str) -> bool:
        if len(number_str) != 9:
            return False

        res = sum(i * int(number_str[-i]) for i in range(1, 10))

        return res % 11 == 0

    def check_account_valid(self, number_str: str) -> str:
        if not number_str.isdigit():
            return "ILL"

        return "" if self.checksum(number_str) else "ERR"

    def check_accounts(self, accounts: List[str]):
        return [" ".join([account, self.check_account_valid(account)]) if self.check_account_valid(account) else account for account in accounts]


class TestOCR:
    def test_read_file_0_should_return_0(self):
        assert OCR().read("digits/0.txt") == ["0"]

    def test_read_file_1_should_return_1(self):
        assert OCR().read("digits/1.txt") == ["1"]

    def test_read_file_2_should_return_2(self):
        assert OCR().read("digits/2.txt") == ["2"]
        
    def test_read_file_3_should_return_3(self):
        assert OCR().read("digits/3.txt") == ["3"]

    def test_read_file_4_should_return_4(self):
        assert OCR().read("digits/4.txt") == ["4"]

    def test_read_file_5_should_return_5(self):
        assert OCR().read("digits/5.txt") == ["5"]
        
    def test_read_file_6_should_return_6(self):
        assert OCR().read("digits/6.txt") == ["6"]

    def test_read_file_7_should_return_7(self):
        assert OCR().read("digits/7.txt") == ["7"]

    def test_read_file_8_should_return_8(self):
        assert OCR().read("digits/8.txt") == ["8"]

    def test_read_file_9_should_return_9(self):
        assert OCR().read("digits/9.txt") == ["9"]

    def test_read_file_unvalid_digit_should_return_ill(self):
        assert OCR().read("digits/unvalid_digit.txt") == ["?"]

    def test_read_file_123456789_should_return_123456789(self):
        assert OCR().read("fixtures/123456789.txt") == ["123456789"]

    def test_read_file_use_case_1_should_return_a_list_of_digits(self):
        result = [str(i) * 9 for i in range(10)] + ["123456789"]
        assert OCR().read("fixtures/use_case_1.txt") == result

    def test_checksum_123456789_should_return_true(self):
        assert OCR().checksum("123456789")

    def test_checksum_111111111_should_return_false(self):
        assert not OCR().checksum("111111111")

    def test_check_account_valid_123456789_should_return_empty_string(self):
        assert OCR().check_account_valid("123456789") == ""

    def test_check_account_valid_111111111_should_return_err(self):
        assert OCR().check_account_valid("111111111") == "ERR"

    def test_check_account_valid_with_non_digits_should_return_ill(self):
        assert OCR().check_account_valid("11111??11") == "ILL"

    def test_check_accounts_should_return_list(self):
        accounts = ["457508000", "664371495", "86110??36"]
        expected_output = ["457508000", "664371495 ERR", "86110??36 ILL"]
        assert OCR().check_accounts(accounts) == expected_output
