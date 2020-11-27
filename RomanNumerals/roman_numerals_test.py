from RomanNumerals.roman_numerals import RomanNumeral


class TestRomanNumeral:
    def test_converting_one_to_roman_should_return_i(self):
        assert RomanNumeral.convert_to_roman_numeral() == "I"

    def test_converting_two_to_roman_should_return_ii(self):
        assert RomanNumeral.convert_to_roman_numeral() == "II"

    def test_converting_three_to_roman_should_return_iii(self):
        assert RomanNumeral.convert_to_roman_numeral() == "III"

    def test_converting_four_to_roman_should_return_iv(self):
        assert RomanNumeral.convert_to_roman_numeral() == "IV"

    def test_converting_five_to_roman_should_return_v(self):
        assert RomanNumeral.convert_to_roman_numeral() == "V"

    def test_converting_six_to_roman_should_return_vi(self):
        assert RomanNumeral.convert_to_roman_numeral() == "VI"

    def test_converting_seven_to_roman_should_return_vii(self):
        assert RomanNumeral.convert_to_roman_numeral() == "VII"

    def test_converting_eight_to_roman_should_return_viii(self):
        assert RomanNumeral.convert_to_roman_numeral() == "VIII"

    def test_converting_nine_to_roman_should_return_ix(self):
        assert RomanNumeral.convert_to_roman_numeral() == "IX"

    def test_converting_ten_to_roman_should_return_x(self):
        assert RomanNumeral.convert_to_roman_numeral() == "X"

    def test_converting_eleven_to_roman_should_return_xi(self):
        assert RomanNumeral.convert_to_roman_numeral() == "XI"

    def test_converting_fourteen_to_roman_should_return_xiv(self):
        assert RomanNumeral.convert_to_roman_numeral() == "XIV"

    def test_converting_nineteen_to_roman_should_return_xix(self):
        assert RomanNumeral.convert_to_roman_numeral() == "XIX"

    def test_converting_forty_nine_to_roman_should_return_xlix(self):
        assert RomanNumeral.convert_to_roman_numeral() == "XLIX"

    def test_converting_1903_to_roman_should_return_mcmiii(self):
        assert RomanNumeral.convert_to_roman_numeral() == "MCMIII"
