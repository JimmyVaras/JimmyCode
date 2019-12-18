import math  # importamos la clase Math para realizar operaciones

# Bucles usando el tipo range TODO

valido = True

email = input("Introduce tu email: ")

for i in range(len(email)):

    if email[i] == "@":

        valido = True

if valido is True:
    print(f"Tu correo es {email}")
else:
    print("Que te den")


# Bucle while

i = 1
while i <= 10:
    print("Ejecutando", str(i))
    i = i+1

edad = int(input("Introduce tu edad: "))

while edad < 0 or edad >= 100:
    print("Edad incorrecta")
    edad = int(input("Introduce tu edad: "))

print(f"Tienes {edad} años")

# Programa de raiz cuadrada con limite de intentos

print("Programa de cálculo de raiz cuadrada")
num = int(input("Introduce el número: "))

intentos = 0
while num < 0:
    print("Raiz imposible")

    if intentos >= 10:
        print("Intentos agotados. Programa finalizado.")
        break;
    num = int(input("Introduce el número: "))
    if num < 0:
        intentos = intentos + 1
if intentos < 10:
    solucion = math.sqrt(num)
    print(f"La raiz es {solucion}")
