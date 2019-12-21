import turtle

t = turtle.Turtle()

t.speed(5)
t.forward(100)

nombre = str(input("Me llamo: "))
lado = int(input("largo del lado: "))
n = int(input("lados de un poligono a dibujar: "))
cant = int(input("Cantidad de lados para multis: "))


def square(lado):
    for i in range(4):
        t.forward(lado)
        t.left(90)


def poligono(lado, n):
    for i in range(n):
        t.forward(lado)
        t.left(360/n)


def poligs(cant):
    ladillos = cant
    while ladillos >= 3:
            poligono(100, ladillos)
            ladillos = ladillos - 1


square(lado)
poligono(lado, n)
poligs(cant)

print(f"Gracias {nombre}")

na = str(input("Pulsa enter para acabar"))
