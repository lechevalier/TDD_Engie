ASCII_PATTERNS_ROWS = [
    {
        "": [1, 4],
        " _": [0, 2, 3, 5, 6, 7, 8, 9],
    },
    {
        "  |": [1, 7],
        "| |": [0],
        "|_": [5, 6],
        "|_|": [4, 8, 9],
        " _|": [2, 3],
    },
    {
        "  |": [1, 4, 7],
        " _|": [3, 5, 9],
        "|_|": [0, 6, 8],
        "|_": [2],
    },
]


class OCR:

    @classmethod
    def read(cls, file_path: str) -> int:
        candidates = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

        with open(file_path) as f:
            print("")
            for i, line in enumerate(f.read().splitlines()):
                print(line)
                candidates.intersection_update(ASCII_PATTERNS_ROWS[i][line])

        assert len(candidates) == 1
        return candidates.pop()


class TestOCR:
    def test_read_file_digit_0_should_return_0(self):
        assert OCR.read("digits/digit_0.txt") == 0

    def test_read_file_digit_1_should_return_1(self):
        assert OCR.read("digits/digit_1.txt") == 1

    def test_read_file_digit_2_should_return_2(self):
        assert OCR.read("digits/digit_2.txt") == 2
        
    def test_read_file_digit_3_should_return_3(self):
        assert OCR.read("digits/digit_3.txt") == 3

    def test_read_file_digit_4_should_return_4(self):
        assert OCR.read("digits/digit_4.txt") == 4

    def test_read_file_digit_5_should_return_5(self):
        assert OCR.read("digits/digit_5.txt") == 5
        
    def test_read_file_digit_6_should_return_6(self):
        assert OCR.read("digits/digit_6.txt") == 6

    def test_read_file_digit_7_should_return_7(self):
        assert OCR.read("digits/digit_7.txt") == 7

    def test_read_file_digit_8_should_return_8(self):
        assert OCR.read("digits/digit_8.txt") == 8

    def test_read_file_digit_9_should_return_9(self):
        assert OCR.read("digits/digit_9.txt") == 9
