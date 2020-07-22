class Car():

    def move(self):
        print("Using my 4 wheels")


class Bike():

    def move(self):
        print("Using my 2 wheels")


class Truck():

    def move(self):
        print("Using my 6 wheels")


class Autobot():
    def move(self):
        print("Using my legs")


def vehiclemove(vehicle):
    vehicle.move()


# Podemos cambiar Optimus entre un camión y un Autobot y seguirá moviendose
# correctamente usando su sistema correspondiente.

Optimus = Autobot()
vehiclemove(Optimus)
