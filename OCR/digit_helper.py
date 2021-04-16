from pathlib import Path
from typing import List, Dict

ASCII_DIGITS = '''\
 _     _  _     _  _  _  _  _ 
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|
'''


def generate_ascii_patterns() -> List[Dict[str, List[str]]]:
    patterns = []
    for line in ASCII_DIGITS.splitlines():
        table = {}
        for digit in range(10):
            table.setdefault(line[digit*3: (digit+1)*3], []).append(str(digit))
        patterns.append(table)
    return patterns


def generate_digit_files(path: Path):
    columns = iter(zip(*ASCII_DIGITS.splitlines()))
    for digit, ascii_lines in enumerate(zip(* [columns] * 3)):
        digit_path = path / f'{digit}.txt'
        ascii_repr = '\n'.join(map(''.join, zip(*ascii_lines)))
        digit_path.write_text(ascii_repr)


if __name__ == '__main__':
    directory = Path() / 'digits'
    directory.mkdir(parents=True, exist_ok=True)
    generate_digit_files(directory)
