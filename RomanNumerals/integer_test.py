from RomanNumerals.roman_numerals import RomanNumeral


class TestRomanNumeral:
    def test_converting_i_to_numeral_should_return_1(self):
        assert RomanNumeral.convert_to_numeral("I") == 1

    def test_converting_ii_to_numeral_should_return_2(self):
        assert RomanNumeral.convert_to_numeral("II") == 2

    def test_converting_iii_to_numeral_should_return_3(self):
        assert RomanNumeral.convert_to_numeral("III") == 3

    def test_converting_iv_to_numeral_should_return_4(self):
        assert RomanNumeral.convert_to_numeral("IV") == 4

    def test_converting_v_to_numeral_should_return_5(self):
        assert RomanNumeral.convert_to_numeral("V") == 5

    def test_converting_vi_to_numeral_should_return_6(self):
        assert RomanNumeral.convert_to_numeral("VI") == 6

    def test_converting_vii_to_numeral_should_return_7(self):
        assert RomanNumeral.convert_to_numeral("VII") == 7

    def test_converting_viii_to_numeral_should_return_8(self):
        assert RomanNumeral.convert_to_numeral("VIII") == 8

    def test_converting_ix_to_numeral_should_return_9(self):
        assert RomanNumeral.convert_to_numeral("IX") == 9

    def test_converting_x_to_numeral_should_return_10(self):
        assert RomanNumeral.convert_to_numeral("X") == 10

    def test_converting_xi_to_numeral_should_return_11(self):
        assert RomanNumeral.convert_to_numeral("XI") == 11

    def test_converting_xiv_to_numeral_should_return_14(self):
        assert RomanNumeral.convert_to_numeral("XIV") == 14

    def test_converting_xix_to_numeral_should_return_19(self):
        assert RomanNumeral.convert_to_numeral("XIX") == 19

    def test_converting_xlix_to_numeral_should_return_49(self):
        assert RomanNumeral.convert_to_numeral("XLIX") == 49

    def test_converting_mcmiii_to_numeral_should_return_1903(self):
        assert RomanNumeral.convert_to_numeral("MCMIII") == 1903
