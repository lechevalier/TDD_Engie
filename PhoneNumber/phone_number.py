from dataclasses import dataclass, field
from typing import Tuple, Optional, Dict


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

    def validate_consistency_old(self) -> bool:
        numbers = list(self.phonebook.values())

        for i, num in enumerate(numbers):
            if i == 0:
                continue
            if not self.validate_sub_consistency(num, numbers[:i]):
                return False

        return True

    def get_inconsistent_number_old(self) -> Tuple:
        numbers = list(self.phonebook.values())

        for i, num in enumerate(numbers):
            if i == 0:
                continue
            if not self.validate_sub_consistency(num, numbers[:i]):
                name = list(self.phonebook.keys())[i]
                return name, num

    def get_inconsistent_number(self) -> Tuple:
        numbers = sorted((number, name) for name, number in self.phonebook.items())
        for i in range(len(numbers) - 1):
            if numbers[i+1][0].startswith(numbers[i][0]):
                return numbers[i][::-1]

    def validate_consistency(self) -> bool:
        return not self.get_inconsistent_number()


@dataclass
class PhoneNumberNode:
    digit: Optional[str] = None
    name: Optional[str] = None
    children: Dict[str, "PhoneNumberNode"] = field(default_factory=dict)
    number: Optional[str] = None

    def __eq__(self, other: "PhoneNumberNode") -> bool:
        return self.digit == other.digit and all(c1 == c2 for c1, c2 in zip(self.children, other.children))

    @property
    def is_prefix_node(self) -> bool:
        return bool(self.name) and bool(self.children)

    def is_consistent(self) -> bool:
        if self.is_prefix_node:
            return False
        return all(child.is_consistent() for child in self.children.values())
    
    def get_inconsistent_node(self) -> Tuple:
        if self.is_prefix_node:
            return self.name, self.number
        return next((child.get_inconsistent_node() for child in self.children.values()), None)


class PhoneNumberTrie:
    def __init__(self, numbers: dict = None):
        self.root = PhoneNumberNode()
        if numbers:
            for name, number in numbers.items():
                self.parse(name, number.replace(' ', '').replace('-', ''))

    def __eq__(self, other: "PhoneNumberTrie") -> bool:
        return self.root == other.root

    @classmethod
    def from_file(cls, filename: str) -> "PhoneNumberTrie":
        trie = cls()
        with open(filename) as f:
            for i, line in enumerate(f):
                if i > 0:
                    name, number = line.rstrip('\n').split(',')
                    trie.parse(name, number.replace(' ', '').replace('-', ''))
        return trie

    def parse(self, name: str, number: str) -> None:
        actual_node = self.root
        
        for digit in number:
            if digit not in actual_node.children:
                new_node = PhoneNumberNode(digit=digit)
                actual_node.children[digit] = new_node

            actual_node = actual_node.children[digit]

        actual_node.name = name
        actual_node.number = number

    def get_name_from_phone_number(self, number: str):
        actual_node = self.root
        for digit in number:
            if digit not in actual_node.children:
                raise ValueError(f"No name for number {number}")
            actual_node = actual_node.children[digit]
            if actual_node.name:
                return actual_node.name

    def validate_consistency(self) -> bool:
        return self.root.is_consistent()
    
    def get_inconsistent_number(self) -> Tuple:
        return self.root.get_inconsistent_node()

