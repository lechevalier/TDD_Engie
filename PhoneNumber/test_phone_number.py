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
