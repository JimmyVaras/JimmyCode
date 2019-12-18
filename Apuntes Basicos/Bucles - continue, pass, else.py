# Continue

for letra in "Python":
    print(letra)

print(" ")

for letra in "Python":
    if letra == "h":
        continue
    print(letra)

print(" ")

nombre = "Jaime Varas Cáceres"

contador = 0

for i in nombre:
    if i == " ":
        continue
    contador += 1

print(contador)

print(" ")

# Pass

# while True:
#     pass  # ctrl+c


class MiClase:

    pass  # editar más tarde

email = input("Introduce el mail: ")

for i in email:
    if i == "@":
        arroba = True
        break;
else:
    arroba = False

print(arroba)
