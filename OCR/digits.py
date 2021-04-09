from pathlib import Path

ASCII_DIGITS = '''\
 _     _  _     _  _  _  _  _ 
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|
'''


def generate_digits(path: Path):
    columns = iter(zip(*ASCII_DIGITS.splitlines()))
    for digit, ascii_lines in enumerate(zip(* [columns] * 3)):
        digit_path = path / f'{digit}.txt'
        ascii_repr = '\n'.join(map(''.join, zip(*ascii_lines)))
        digit_path.write_text(ascii_repr)


if __name__ == '__main__':
    directory = Path() / 'digits'
    directory.mkdir(parents=True, exist_ok=True)
    generate_digits(directory)
