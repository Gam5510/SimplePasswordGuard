from simplepasswordguard import PasswordGenerator

def test_generate_count():
    gen = PasswordGenerator(length=8, level=2)
    passwords = gen(3)
    assert isinstance(passwords, list)
    assert len(passwords) == 3

def test_strength_check():
    gen = PasswordGenerator(length=10, level=3)
    passwords = gen(2)
    for pwd in passwords:
        assert gen.check_strength(pwd) in ("easy", "medium", "hard")
