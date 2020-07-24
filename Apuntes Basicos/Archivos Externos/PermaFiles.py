import pickle


class save:

    def __init__(self, name, type, lvl):
        self.name = name
        self.type = type
        self.lvl = lvl
        print(f"{self.name} ha sido creado con clase {self.type}"
              f" a nivel {self.lvl}.")

    def __str__(self):
        return "{} {} {}".format(self.name, self.type, self.lvl)


class savelist:

    saves = []

    def __init__(self):
        listSaves = open("data", "ab+")
        listSaves.seek(0)
        try:
            self.saves = pickle.load(listSaves)
            print(f"Se ha guardado el progreso. \n{len(self.saves)} "
                  "partidas guardadas")

        except(EOFError):
            print("No hay partidas guardadas")

        finally:
            listSaves.close()
            del(listSaves)

    def saveAs(self, As):
        self.saves.append(As)

    def seeSaves(self):
        for i in self.saves:
            print(i)

    def savedata(self):
        listSaves = open("data", "wb")
        pickle.dump(self.saves, listSaves)
        listSaves.close()
        del(listSaves)

    def infodata(self):
        print("Estas son las partidas guardadas:")
        for i in self.saves:
            print(i)


list = savelist()

As = save("Jimmy", "comando", "1")
list.saveAs(As)
As = save("Filthy", "Siren", "23")
list.saveAs(As)
As = save("Gearbox", "Zer0", "6")
list.saveAs(As)

# list.seeSaves()

list.savedata()

list.infodata()
