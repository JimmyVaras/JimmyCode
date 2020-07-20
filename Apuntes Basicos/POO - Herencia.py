class personajes():
    def __init__(self, type, name):

        self.type = type
        self.name = name
        self.unlocked = False
        self.level = 0
        self.active = False

    def activate(self):

        self.active = True

    def buylevel(self, num):

        if self.active:
            self.level += num
            print(f"Has alcanzado el nivel {self.level}")

        else:
            print("Contrato no activo, activalo para comprar niveles.")

    def status(self):

        if self.level >= 5:
            self.unlocked = True
        print(f"Tipo: {self.type} \nNombre: {self.name} \nNivel de contrato: {self.level} \nDesbloqueado: {self.unlocked} \nContrato Activo: {self.active}")


class Raze(personajes):
    pass


JimmyRaze = Raze("Duelista", "Raze")

JimmyRaze.activate()

JimmyRaze.buylevel(7)

JimmyRaze.status()
