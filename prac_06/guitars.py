from prac_06.guitar import Guitar


def main():
    my_guitars = []
    print("MY GUITARS! :)\n")
    guitar_name = input("Guitar: ").title()
    while guitar_name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        my_guitars.append(Guitar(guitar_name, year, cost))
        print("{} ({}): ${:.2f} added".format(guitar_name, year, cost))
        guitar_name = input("Guitar: ").title()

    print("....LOADING...\nThese are my guitars: ")
    for i, guitar in enumerate(my_guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print("Guitar {0}: {2.name} ({2.year}), worth ${2.cost:.2f} {1}".format(i, vintage_string, guitar))


main()
