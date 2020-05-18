from Prac_08.taxi import Taxi
from Prac_08.silver_service_taxi import SilverServiceTaxi
TAXIS = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    print('Lets dirve!')
    user_input = get_menu_choice()
    bill = 0.0
    current_taxi = None
    while user_input != 'q':
        if user_input == 'c':
            current_taxi = choose_taxi(bill)
        else:
            bill = drive_taxi(bill, current_taxi)
        user_input = get_menu_choice()
    print("Total trip cost: ${}\nTaxis are now: ".format(bill))
    show_taxis(TAXIS)


def get_menu_choice():
    user_input = input("q)uit, c)hoose taxi, d)rive\n>>>\t").lower()
    return user_input


def show_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def choose_taxi(bill):
    print('Taxis available:')
    show_taxis(TAXIS)
    taxi_choice = int(input("Please choose the taxi from above taxis: "))
    print("Your bill-to-date: $", bill)
    return TAXIS[taxi_choice]


def drive_taxi(bill, current_taxi):
    distance = float(input("Drive how far(in km)? "))
    current_taxi.drive(distance)
    bill += current_taxi.get_fare()
    return bill


main()
