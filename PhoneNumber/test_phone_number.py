from PhoneNumber.phone_number import PhoneNumberTrie as PhoneNumber


class TestPhoneNumber:

    def setup_class(self):
        inconsistent_phonebook = {
            "Bob": "91 12 54 26",
            "Alice": "97 625 992",
            "Emergency": "911",
        }
        self.inconsistent_phone_number = PhoneNumber(inconsistent_phonebook)

        consistent_phonebook = {
            "Bob": "91 12 54 26",
            "Alice": "97 625 992",
            "Emergency": "9110",
        }

        self.consistent_phone_number = PhoneNumber(consistent_phonebook)

    def test_dial_911_should_call_emergency(self):
        assert self.inconsistent_phone_number.get_name_from_phone_number("911") == "Emergency"

    def test_dial_97625992_should_call_alice(self):
        assert self.inconsistent_phone_number.get_name_from_phone_number("97625992") == "Alice"

    def test_dial_91125426_should_call_emergency(self):
        assert self.inconsistent_phone_number.get_name_from_phone_number("91125426") == "Emergency"

    def test_phone_book_egality(self):
        filename = "phone_data_mock.txt"
        phone_mock = PhoneNumber({
            "Bob": "91125426",
            "Alice": "97625992",
            "Emergency": "911",
            "Bobby": "91125426",
            "Alicia": "97625992",
        })
        assert PhoneNumber.from_file(filename) == phone_mock

    def test_validate_phone_book_consistency_returns_false_when_numbers_are_inconsistent(self):
        assert not self.inconsistent_phone_number.validate_consistency()

    def test_get_inconsistent_number_returns_the_first_inconsistent_number_when_phone_book_is_inconsistent(self):
        assert self.inconsistent_phone_number.get_inconsistent_number() == ("Emergency", "911")

    def test_validate_phone_book_consistency_returns_true_when_numbers_are_consistent(self):
        print(self.consistent_phone_number.validate_consistency())
        assert self.consistent_phone_number.validate_consistency()

    def test_validate_phone_book_10000_consistency_returns_true_when_numbers_are_consistent(self):
        assert not PhoneNumber.from_file("phone_data_10000.txt").validate_consistency()

    def test_validate_phone_book_65535_consistency_returns_true_when_numbers_are_consistent(self):
        assert not PhoneNumber.from_file("phone_data_65535.txt").validate_consistency()

    def test_validate_phone_book_consistent_returns_true(self):
        assert PhoneNumber.from_file("phone_data_65535_consistent.txt").validate_consistency()


class TestPhoneNumberOld(TestPhoneNumber):
    pass
