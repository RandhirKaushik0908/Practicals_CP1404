"""
Password Checker
"""

MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""

    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain:")
    print("\t1 or more uppercase characters\n\t1 or more lowercase characters\n\t1 or more numbers")
    print("\tand 1 or more special characters from: ", SPECIAL_CHARACTERS)
    password = input("--> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("--> ")
    print("Your {}-character password is valid: {}".format(len(password), password))


def is_valid_password(password):
    """Determine if the provided password is valid."""

    while MIN_LENGTH >= len(password) >= MAX_LENGTH:
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.islower():
            count_lower += 1
        if char.isupper():
            count_upper += 1
        if char.isdigit():
            count_digit += 1
        if char in SPECIAL_CHARACTERS:
            count_special += 1
    if count_lower == 0 or count_upper == 0 or count_digit == 0 or count_special == 0:
        return False
    # Will return False if it's zero
    # if we get here (without returning False), then the password must be valid
    return True


main()
