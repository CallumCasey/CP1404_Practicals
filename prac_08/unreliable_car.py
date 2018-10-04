from Prac_08.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that includes unreliability"""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance. """
        self.reliability = reliability
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        """Return a string representation of a Car object."""
        return "{}, fuel={}, odometer={}".format(self.name, self.fuel,
                                                 self.odometer)

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        random_reliability = random.randint(0, 100)

        if random_reliability > self.reliability:
            distance = 0
        else:
            pass

        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance
