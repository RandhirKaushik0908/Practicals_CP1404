from Prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    limo_taxi = SilverServiceTaxi('Limo', 200, 2)
    print(limo_taxi)
    limo_taxi.drive(18)
    print(limo_taxi)
    print("Current Fare: $", limo_taxi.get_fare())


main()
