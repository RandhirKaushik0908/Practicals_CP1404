from Prac_08.unreliable_car import UnreliableCar


def main():
    unreliable_car = UnreliableCar('Mazda', 100, 50.123)
    print("This is an unreliable car: \n\t", unreliable_car)
    unreliable_car.drive(75)
    print("Tried to drive unreliable car for 75km. Let's see the if its possible(odometer): \n\t", unreliable_car)
    unreliable_car.add_fuel(50)
    print("Added 50 units fuel: \n\t", unreliable_car)
    unreliable_car.drive(50)
    print("Tried to drive unreliable car for another 50km. Let's see the if its possible(odometer): \n\t", unreliable_car)


main()
