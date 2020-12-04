class PhoneNumber:
    def __init__(self, phonebook):
        self.phonebook = {name: number.replace(' ', '') for name, number in phonebook.items()}

    def get_name_from_phone_number(self, number: str):
        candidates = []
        for book_name, book_number in self.phonebook.items():
            if number.startswith(book_number):
                candidates.append(book_name)
        return min(candidates, key=lambda name: len(self.phonebook[name]))
