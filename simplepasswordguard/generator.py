import random
import string
import datetime
from typing import List, Union, Dict, Iterator

class PasswordGenerator:
    def __init__(self, length: int, level: int):
        """
        Initialize the password generator.
        
        :param length: Length of each password.
        :param level: Complexity level (1=easy, 2=medium, 3=hard).
        """
        self.length = length
        self.level = level
        self.symbols = self.get_symbols()
        self.passwords: List[str] = []

    def get_symbols(self) -> str:
        """Select symbols based on the complexity level."""
        if self.level == 1:
            return string.ascii_letters
        elif self.level == 2:
            return string.ascii_letters + string.digits
        elif self.level == 3:
            return string.ascii_letters + string.digits + string.punctuation
        else:
            raise ValueError("Invalid password level")

    def generate_password(self) -> str:
        """Generate a single password matching the complexity level."""
        level_map = {1: "easy", 2: "medium", 3: "hard"}

        while True:
            password = ''.join(random.choice(self.symbols) for _ in range(self.length))
            if self.check_strength(password) == level_map[self.level]:
                return password

    def generate_many_password(self, count: int = 1) -> List[str]:
        """Generate multiple passwords."""
        self.passwords = [self.generate_password() for _ in range(count)]
        return self.passwords

    def check_strength(self, passwords: Union[str, List[str], tuple]) -> Union[str, Dict[str, str]]:
        """Check the strength of a password or a list of passwords."""
        def _check_one(password: str) -> str:
            has_digit = any(c in string.digits for c in password)
            has_letter = any(c in string.ascii_letters for c in password)
            has_symbol = any(c in string.punctuation for c in password)

            if has_digit and has_letter and has_symbol:
                return "hard"
            elif (has_digit and has_letter) or (has_digit and has_symbol) or (has_letter and has_symbol):
                return "medium"
            else:
                return "easy"

        if isinstance(passwords, str):
            return _check_one(passwords)
        elif isinstance(passwords, (list, tuple)):
            return {password: _check_one(password) for password in passwords}
        else:
            raise TypeError("Argument must be a string or a list/tuple of strings")

    def save_file(self, passwords: List[str], filename: str = "passwords.txt", mode: str = "a") -> None:
        """Save passwords to a file."""
        with open(filename, mode, encoding="utf-8") as file:
            file.write(f"\n=== {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n")
            file.write(f"{self}\n")
            for n, password in enumerate(passwords, 1):
                file.write(f"{n}) {password}\n")

    def print_terminal(self, passwords: List[str]) -> None:
        """Print passwords to the terminal."""
        print(f"{self}")
        for n, password in enumerate(passwords, 1):
            print(f"{n}) {password}")

    def __iter__(self) -> Iterator[str]:
        """Generator for iterating passwords. Infinite if max_count=None."""
        while True:
            yield self.generate_password()

    def __call__(self, count: int = 1) -> List[str]:
        """Generate passwords by calling the object."""
        return self.generate_many_password(count)

    def to_list(self, count: int = 5) -> List[str]:
        """Return a list of generated passwords."""
        return self.generate_many_password(count)

    def __str__(self) -> str:
        levels = {1: "easy", 2: "medium", 3: "hard"}
        level_name = levels.get(self.level, "unknown")
        return f"PasswordGenerator(length={self.length}, level={self.level} [{level_name}])"

    def __repr__(self) -> str:
        return f"PasswordGenerator(length={self.length}, level={self.level})"

