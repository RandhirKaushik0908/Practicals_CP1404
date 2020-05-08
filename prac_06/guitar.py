class Guitar:
    """ Represents a guitar object. """

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : $ {}".format(self.name, self.year, self.cost)

    def get_age(self):
        CURRENT_YEAR = 2020
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        age = self.get_age()
        if age >= 50:
            return True
        else:
            return False
