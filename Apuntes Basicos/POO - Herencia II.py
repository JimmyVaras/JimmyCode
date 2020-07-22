import time
import random


class vehicle():
    def __init__(self, brand, model, terrain):

        self.brand = brand
        self.model = model
        self.terrain = terrain
        self.on = False

    def start(self):

        self.on = True
        print("\nEl motor ha sido arrancado")
        time.sleep(1)
        self.status()

    def status(self):
        if self.on:
            engine = "Arrancado"
        else:
            engine = "Apagado"

        print(f"\nMarca: {self.brand} \nModelo: {self.model} \nFunciona en {self.terrain} \nMotor: {engine}")


class Car(vehicle):

    def register(self):

        seats = input(f"¿Cuantos asientos tiene el {self.brand} {self.model}?: ")
        return seats

    def status(self):

        if self.on:
            engine = "Arrancado"
        else:
            engine = "Apagado"

        print(f"\nMarca: {self.brand} \nModelo: {self.model} \nFunciona en {self.terrain} \nMotor: {engine} \nAsientos: {EMX} \n")
        time.sleep(1)


class ElectricVehicle():
    def __init__(self):
        self.battery = 0
        self.charging = False

    def charge(self):
        if self.charging:
            self.charging = False

        else:
            self.charging = True

        while self.charging is True and self.battery < 100:
            self.battery += random.randint(5,14)
            print(f"Batería: {self.battery}% \n")
            time.sleep(0.8)
        if self.battery >= 100:
            print("------Batería cargada con éxito------ \n")

    def status(self):
        print(f"Batería al {self.battery}% \n")


ElonMust = Car("Tesla", "Model Y", "carretera")


class ElectricCar(Car, ElectricVehicle):
    pass


EMX = ElonMust.register()
time.sleep(1.5)
ElonMust.start()

BiciElectrica = ElectricVehicle()

BiciElectrica.status()
time.sleep(0.2)
print("Enchufando bici eléctrica para cargar...")
time.sleep(0.5)
print(".")
time.sleep(0.3)
print(".")
time.sleep(0.3)
print(".")
time.sleep(0.3)
time.sleep(0.2)
BiciElectrica.charge()
