from Prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability=0.0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if randint(0, 100) > self.reliability:
            distance = 0
        super().drive(distance)
        return distance
