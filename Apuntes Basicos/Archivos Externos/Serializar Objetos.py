import pickle


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
        print(f"Tipo: {self.type} \nNombre: {self.name} \nNivel de contrato:"
              f" {self.level} \nDesbloqueado: {self.unlocked}"
              f"\nContrato Activo: {self.active}")


main = personajes("Entry", "Raze")
healer = personajes("Support", "Sage")
smoker = personajes("Control", "Brimstone")

picks = [main, healer, smoker]

bfile = open("Jimmy#000", "wb")
pickle.dump(picks, bfile)

bfile.close()

openfile = open("Jimmy#000", "rb")
picks = pickle.load(openfile)
openfile.close()

for i in picks:
    print(i.status())
