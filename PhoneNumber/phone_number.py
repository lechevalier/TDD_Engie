PHONE_BOOK = [
            ("Bob", "91 12 54 26"),
            ("Alice", "97 625 992"),
            ("Emergency", "911")
        ]


class PhoneNumber:
    @classmethod
    def get_name_from_phone_number(cls, number: str):
        return "Emergency"

