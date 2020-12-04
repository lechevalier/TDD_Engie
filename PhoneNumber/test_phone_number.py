from PhoneNumber.phone_number import PhoneNumber


class TestPhoneNumber:

    def setup_class(self):
        self.phone_number = PhoneNumber()

    def test_dial_911_should_call_emergency(self):
        self.phone_number.get_name_from_phone_number("911")