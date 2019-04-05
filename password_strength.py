from getpass import getpass

LONG_LENGTH = 15
DIVERSE_COUNT = 6


def has_digit(password):
    return any([char.isdigit() for char in password])


def is_very_long(password):
    return len(password) >= LONG_LENGTH


def is_diverse(password):
    return len(set(password)) > DIVERSE_COUNT


def has_letters(password):
    return any([char.isalpha() for char in password])


def has_upper_letters(password):
    return any([char.isupper() for char in password])


def has_lower_letters(password):
    return any([char.islower() for char in password])


def has_symbols(password):
    return not password.isalnum()


def has_not_only_symbols(password):
    return password.isalnum()


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
        strength += check(password)
    return strength, len(checks)


def main():
    print("Введите пароль:")
    password = getpass()
    print("Надежность пароля: {}/{}".format(*get_password_strength(password)))

if __name__ == "__main__":
    main()
