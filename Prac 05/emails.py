def main():
    email_to_name = {}
    email_address = input("Please enter your email: ")

    while email_address != '':
        name = get_name(email_address)
        name_confirmation = input("Is " + name + " your name? (Press Enter or type Y for yes; any other input for no.)")
        if name_confirmation != "" and name_confirmation.upper() != "Y":
            name = input("Please enter your name: ".title())
            while len(name) == 0:
                name = input("Error! Please enter your name: ").title()

        email_to_name[email_address] = name
        email_address = input("Please enter your email: ")

    print("\nEmails and Names:\n")
    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


def get_name(email_address):
    full_name = email_address.split('@')[0]
    name_parts = full_name.split('.')
    name = ' '.join(name_parts)
    return name.title()


main()
