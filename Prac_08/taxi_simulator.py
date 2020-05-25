from Prac_08.silver_service_taxi import SilverServiceTaxi
from Prac_08.taxi import Taxi

TAXIS = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    print('Lets drive!')
    user_input = get_menu_choice()
    total_bill = 0.0
    current_taxi = None
    while user_input != 'q':
        if user_input == 'c':
            current_taxi, bill = choose_taxi(total_bill)
            total_bill += bill
        elif user_input == 'd':
            if current_taxi is None:
                print("Please select a taxi first!")
            else:
                bill = drive_taxi(current_taxi)
                print("Your bill for this trip: ${}".format(bill))
                total_bill += bill
        else:
            print("Invalid Input! Choose from the given menu choices only.")
        print("Your bill-to-date: $", total_bill)
        user_input = get_menu_choice()
    print("Total trip cost: ${}\nTaxis are now: ".format(total_bill))
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
    return TAXIS[taxi_choice], bill


def drive_taxi(current_taxi):
    trip_bill = 0
    current_taxi.start_fare()
    distance = float(input("Drive how far(in km)? "))
    current_taxi.drive(distance)
    trip_bill += current_taxi.get_fare()
    return trip_bill


main()
