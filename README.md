# passwordgen

**simplepasswordguard** is a simple Python library for generating secure passwords.  
You can create single or multiple passwords, check their strength, print them, or save to a file.

---

## Features

- Generate passwords of any length  
- Three complexity levels:
  - **Easy:** letters only  
  - **Medium:** letters + digits  
  - **Hard:** letters + digits + symbols  
- Generate multiple passwords at once  
- Check password strength  
- Print passwords to terminal  
- Save passwords to a file with timestamp  
- Infinite generator for iterative password creation  

---

## Installation

Install from PyPI:

```bash
pip install simplepasswordguard
```



## Quick Start
```python
from simplepasswordguard import PasswordGenerator

# Create a password generator: 12 characters, hard level
gen = PasswordGenerator(length=12, level=3)

# Generate a single password
print(gen.generate_password())

# Generate multiple passwords
print(gen.generate_many_password(5))

# Use the object as a callable
print(gen(3))

# Save passwords to a file
gen.save_file(["password1", "password2"], filename="my_passwords.txt")

# Print passwords to terminal
gen.print_terminal(["password1", "password2"])

# Check password strength
print(gen.check_strength("Abc123!"))
print(gen.check_strength(["abc123", "A1!b2C3"]))
```

## API

### Constructor
`PasswordGenerator(length: int, level: int)`

- **length**: number of characters in each password
- **level**: complexity:
  - 1 → Easy (letters only)
  - 2 → Medium (letters + digits)
  - 3 → Hard (letters + digits + symbols)

### Key Methods
- `generate_password()` — generate a single password
- `generate_many_password(count)` — generate multiple passwords
- `check_strength(passwords)` — check password strength (easy, medium, hard)
- `save_file(passwords, filename)` — save passwords to a file
- `print_terminal(passwords)` — print passwords to the terminal
- `__call__(count)` — generate passwords using the object itself
- `to_list(count)` — get a list of generated passwords
- `__iter__()` — infinite password generator

