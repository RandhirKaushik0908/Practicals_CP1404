from Prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """ A version or type of car that can be drive on basis of its reliability. """

    def __init__(self, name, fuel, reliability=0.0):
        """ Initialise an instance of unreliable car, based on the parent class Car. """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """ Drives like its parent car, but depending on its reliability randomly. """
        if randint(0, 100) > self.reliability:
            distance = 0
        super().drive(distance)
        return distance
