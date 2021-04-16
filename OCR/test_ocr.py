from typing import List

from OCR.digit_helper import generate_ascii_patterns

ASCII_PATTERNS_ROWS = generate_ascii_patterns()


class OCR:

    def sanitize(self, input: str) -> str:
        lines = input.splitlines()
        max_length = max(map(len, lines))
        return '\n'.join(line.ljust(max_length) for line in lines)

    def print_entry(self, entry):
        for digit in entry:
            print('\n'.join(digit))
            print()

    def read(self, file_path: str) -> str:
        with open(file_path) as f:
            lines = self.sanitize(f.read()).splitlines()
            assert lines
            entry = [[line[i: i+3] for line in lines] for i in range(0, len(lines[0]), 3)]
            if True:
                self.print_entry(entry)
            return ''.join(str(self.read_digit(digit)) for digit in entry)

    def read_digit(self, ascii_chars: List[str]):
        candidates = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        for i, ascii in enumerate(ascii_chars):
            candidates.intersection_update(ASCII_PATTERNS_ROWS[i][ascii])
        assert len(candidates) == 1
        return candidates.pop()


class TestOCR:
    def test_read_file_0_should_return_0(self):
        assert OCR().read("digits/0.txt") == "0"

    def test_read_file_1_should_return_1(self):
        assert OCR().read("digits/1.txt") == "1"

    def test_read_file_2_should_return_2(self):
        assert OCR().read("digits/2.txt") == "2"
        
    def test_read_file_3_should_return_3(self):
        assert OCR().read("digits/3.txt") == "3"

    def test_read_file_4_should_return_4(self):
        assert OCR().read("digits/4.txt") == "4"

    def test_read_file_5_should_return_5(self):
        assert OCR().read("digits/5.txt") == "5"
        
    def test_read_file_6_should_return_6(self):
        assert OCR().read("digits/6.txt") == "6"

    def test_read_file_7_should_return_7(self):
        assert OCR().read("digits/7.txt") == "7"

    def test_read_file_8_should_return_8(self):
        assert OCR().read("digits/8.txt") == "8"

    def test_read_file_9_should_return_9(self):
        assert OCR().read("digits/9.txt") == "9"

    def test_read_file_9_should_return_123456789(self):
        assert OCR().read("fixtures/123456789.txt") == "123456789"
