from typing import Tuple


class PhoneNumber:
    def __init__(self, phonebook):
        self.phonebook = {name: number.replace(' ', '').replace('-', '') for name, number in phonebook.items()}

    def __eq__(self, other: "PhoneNumber"):
        return other.phonebook == self.phonebook

    @classmethod
    def from_file(cls, filename) -> "PhoneNumber":
        with open(filename) as f:
            phone_book = {}
            for i, line in enumerate(f):
                if i > 0:
                    name, number = line.rstrip('\n').split(',')
                    phone_book[name] = number
        return cls(phone_book)

    def get_name_from_phone_number(self, number: str):
        candidates = []
        for book_name, book_number in self.phonebook.items():
            if number.startswith(book_number):
                candidates.append(book_name)
        return min(candidates, key=lambda name: len(self.phonebook[name]))

    @staticmethod
    def validate_sub_consistency(number: str, numbers: list) -> bool:
        return not any(nb.startswith(number) or number.startswith(nb) for nb in numbers)

    def validate_consistency(self) -> bool:
        numbers = list(self.phonebook.values())

        for i, num in enumerate(numbers):
            if i == 0:
                continue
            if not self.validate_sub_consistency(num, numbers[:i]):
                return False

        return True

    def get_inconsistent_number(self) -> Tuple:
        numbers = list(self.phonebook.values())

        for i, num in enumerate(numbers):
            if i == 0:
                continue
            if not self.validate_sub_consistency(num, numbers[:i]):
                name = list(self.phonebook.keys())[i]
                return name, num

        return None
