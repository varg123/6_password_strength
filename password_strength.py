from getpass import getpass

LONG_LENGTH = 15
DIVERSE_COUNT = 6


def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False


def is_very_long(password):
    if len(password) >= LONG_LENGTH:
        return True
    return False


def is_diverse(password):
    return len(set(password)) > DIVERSE_COUNT


def has_letters(password):
    for char in password:
        if not char.isdigit():
            return True
    return False


def has_upper_letters(password):
    for char in password:
        if char.isupper():
            return True
    return False


def has_lower_letters(password):
    for char in password:
        if char.islower():
            return True
    return False


def has_symbols(password):
    if not password.isalnum():
            return True
    return False


def has_not_only_symbols(password):
    if password.isalnum():
        return True
    return False


def get_password_strength(password):
    strength = 0
    checks = [
        is_very_long,
        is_diverse,
        has_digit,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
    ]
    for check in checks:
        if check(password):
            strength += 1
    return strength, len(checks)


def main():
    print("Введите пароль:")
    password = getpass()
    print("Надежность пароля: {}/{}".format(*get_password_strength(password)))

if __name__ == "__main__":
    main()
