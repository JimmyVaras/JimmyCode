# http://pyspanishdoc.sourceforge.net/lib/string-methods.html

# Transformar un string entero en mayúsculas

mayus = input("Introduce en minúsculas: ")
print(mayus.upper())

# Transformar un string entero en minúsculas

minus = input("Introduce en mayúsculas: ")
print(minus.lower())

# Poner la primera letra en mayúsculas

ugly = input("Introduce tu nombre en minúsculas: ")
print(ugly.capitalize())

# Cuenta cuantas veces aparece X caracter en un string

word1 = input("Escribe una palabra con la letra A: ")
print("Tu palabra tiene la letra 'A'", word1.count("a"), "veces")

# Señala la posición de X caracter dentro de un string

mail = input("Introduce tu correo: ")
arroba = mail.find("@")
#print("El arroba se encuentra en la posición", arroba)
print("Tu nombre de usuario será:", mail[:arroba].capitalize())

# Comprobar que son digitos.

age1 = input("Introduce tu edad: ")

while age1.isdigit() is False:
    print("Introduce un valor numérico")
    age1 = input("Introduce tu edad: ")

print("Tu edad es:", age1)

# Comprobar que son letras (espacios no admitidos)

name1 = input("Introduce tu nombre: ")

while age1.isalpha() is False:
    print("No se permiten numeros ni espacios")
    age1 = input("Introduce tu nombre: ")

print("Tu nombre es:", name1)

# Separa un string buscando espacios o lo que se especifique.

sentence = input("Introduce una frase: ")
print(sentence.split())

# Borrar espacios al final de un string

print(sentence.strip())
