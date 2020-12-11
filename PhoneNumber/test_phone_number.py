from PhoneNumber.phone_number import PhoneNumber


class TestPhoneNumber:

    def setup_class(self):
        phonebook = {
            "Bob": "91 12 54 26",
            "Alice": "97 625 992",
            "Emergency": "911",
        }
        self.phone_number = PhoneNumber(phonebook)

    def test_dial_911_should_call_emergency(self):
        assert self.phone_number.get_name_from_phone_number("911") == "Emergency"

    def test_dial_97625992_should_call_alice(self):
        assert self.phone_number.get_name_from_phone_number("97625992") == "Alice"

    def test_dial_91125426_should_call_emergency(self):
        assert self.phone_number.get_name_from_phone_number("91125426") == "Emergency"

    def test_parsing_phone_book_file_returns_a_dictionary(self):
        filename = "phone_data_mock.txt"
        phone_mock = PhoneNumber({
            "Bob": "91125426",
            "Alice": "97625992",
            "Emergency": "911",
            "Bobby": "91125426",
            "Alicia": "97625992",
        })
        assert self.phone_number.from_file(filename) == phone_mock

    def test_validate_phone_book_consistency_returns_False(self):
        assert not self.phone_number.validate_consistency()
