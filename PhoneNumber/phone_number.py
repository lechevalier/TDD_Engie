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

    def validate_consistency(self) -> bool:
        numbers = self.phonebook.values()
        for num in numbers:
            if any(nb.startswith(num) for nb in numbers if nb != num):
                return False
        return True
