ROMAN_NUMERALS = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}


class RomanNumeral:
    @classmethod
    def convert(cls, number):
        roman_numeral = ""
        for n, s in ROMAN_NUMERALS.items():
            while number >= n:
                roman_numeral += s
                number -= n
        return roman_numeral


class TestRomanNumeral:
    def test_converting_one_to_roman_should_return_i(self):
        assert RomanNumeral.convert(1) == "I"

    def test_converting_two_to_roman_should_return_ii(self):
        assert RomanNumeral.convert(2) == "II"

    def test_converting_three_to_roman_should_return_iii(self):
        assert RomanNumeral.convert(3) == "III"

    def test_converting_four_to_roman_should_return_iv(self):
        assert RomanNumeral.convert(4) == "IV"

    def test_converting_five_to_roman_should_return_v(self):
        assert RomanNumeral.convert(5) == "V"

    def test_contest_converting_six_to_roman_should_return_vi(self):
        assert RomanNumeral.convert(6) == "VI"

    def test_contest_converting_seven_to_roman_should_return_vii(self):
        assert RomanNumeral.convert(7) == "VII"

    def test_contest_converting_eight_to_roman_should_return_viii(self):
        assert RomanNumeral.convert(8) == "VIII"

    def test_contest_converting_nine_to_roman_should_return_ix(self):
        assert RomanNumeral.convert(9) == "IX"

    def test_contest_converting_ten_to_roman_should_return_x(self):
        assert RomanNumeral.convert(10) == "X"

    def test_contest_converting_eleven_to_roman_should_return_xi(self):
        assert RomanNumeral.convert(11) == "XI"

    def test_contest_converting_fourteen_to_roman_should_return_xiv(self):
        assert RomanNumeral.convert(14) == "XIV"

    def test_contest_converting_nineteen_to_roman_should_return_xix(self):
        assert RomanNumeral.convert(19) == "XIX"

    def test_contest_converting_forty_nine_to_roman_should_return_xlix(self):
        assert RomanNumeral.convert(49) == "XLIX"

    def test_contest_converting_1903_to_roman_should_return_mcmiii(self):
        assert RomanNumeral.convert(1903) == "MCMIII"
