MIN_LENGTH = 5


def main():
    password = get_password()
    show_asterisks(password)


def get_password():
    password = input("Please enter your password: ")
    while len(password) < 5:
        password = input("ERROR! Please enter your {}-digit password: ".format(MIN_LENGTH))
    return password


def show_asterisks(password):
    for i in range(len(password)):
        print("*", end="")


main()
