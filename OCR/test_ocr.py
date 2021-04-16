ASCII_PATTERNS_ROWS = [
    {
        "   ": [1, 4],
        " _ ": [0, 2, 3, 5, 6, 7, 8, 9],
    },
    {
        "  |": [1, 7],
        "| |": [0],
        "|_ ": [5, 6],
        "|_|": [4, 8, 9],
        " _|": [2, 3],
    },
    {
        "  |": [1, 4, 7],
        " _|": [3, 5, 9],
        "|_|": [0, 6, 8],
        "|_ ": [2],
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
    def test_read_file_0_should_return_0(self):
        assert OCR.read("digits/0.txt") == 0

    def test_read_file_1_should_return_1(self):
        assert OCR.read("digits/1.txt") == 1

    def test_read_file_2_should_return_2(self):
        assert OCR.read("digits/2.txt") == 2
        
    def test_read_file_3_should_return_3(self):
        assert OCR.read("digits/3.txt") == 3

    def test_read_file_4_should_return_4(self):
        assert OCR.read("digits/4.txt") == 4

    def test_read_file_5_should_return_5(self):
        assert OCR.read("digits/5.txt") == 5
        
    def test_read_file_6_should_return_6(self):
        assert OCR.read("digits/6.txt") == 6

    def test_read_file_7_should_return_7(self):
        assert OCR.read("digits/7.txt") == 7

    def test_read_file_8_should_return_8(self):
        assert OCR.read("digits/8.txt") == 8

    def test_read_file_9_should_return_9(self):
        assert OCR.read("digits/9.txt") == 9
