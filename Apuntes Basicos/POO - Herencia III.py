class Person():
    def __init__(self, name, age, country):

        self.name = name
        self.age = age
        self.country = country

    def info(self):

        print(f"\n   Nombre: {self.name}\n   Edad: {self.age}\n   País: {self.country}\n")


class Youtuber(Person):
    def __init__(self, subs, views, nameyt, ageyt, countryyt):
        super().__init__(nameyt, ageyt, countryyt)

        self.subs = subs
        self.views = views

    def info(self):

        super().info()
        print(f"   {self.name} tiene un canal con {self.subs} y un total de {self.views}.\n")


Jimmy = Youtuber(27, 828, "Jaime", 17, "España")

Jimmy.info()

# Comprobamos con isinstance si "Jimmy" pertenece a la clase "Youtuber"

print(isinstance(Jimmy, Person))

# Devolverá True si es cierto

# Comprobamos además si "Jimmy" pertenece a la clase "Youtuber"

print(isinstance(Jimmy, Person))

# Ahora Bartolo:

Bartolo = Person("Bartolo", 57, "Perú")

# Vamos a confirmar que Bartolo es persona pero no es un Youtuber

print(isinstance(Bartolo, Person))
print(isinstance(Bartolo, Youtuber))
