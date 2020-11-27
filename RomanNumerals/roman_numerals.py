# Order matters
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
NUMERAL_ROMANS = dict(map(reversed, ROMAN_NUMERALS.items()))


class RomanNumeral:
    @staticmethod
    def convert_to_roman_numeral(number):
        roman_numeral = ""
        for n, s in ROMAN_NUMERALS.items():
            while number >= n:
                roman_numeral += s
                number -= n
        return roman_numeral

    @staticmethod
    def convert_to_numeral(text):
        number = 0
        sub_text = text[:]
        for s, n in NUMERAL_ROMANS.items():
            while sub_text.startswith(s):
                sub_text = sub_text[len(s):]
                number += n
        return number
