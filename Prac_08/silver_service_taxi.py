from Prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """ A specialized and fancier type of taxi(and ultimately, car). """
    flagfall = 4.50     # class variable

    def __init__(self, name, fuel, fanciness=0.0):
        """ Initialise an instance of Silver Service taxi, based on the parent class Taxi(Car)."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the price for the taxi trip."""
        total_fare = self.flagfall + super().get_fare()
        return total_fare

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)
