print("Vamos a evaluar las probabilidades de obtener la beca en base a las siguientes condiciones: Distancia al centro, familia numerosa y el salario familiar.")

distancia=int(input("Introduce la distancia a la escuela en km:"))
print("Te encuentras a", distancia, "kms de la escuela")

hermanos=int(input("Número de hermanos:"))
print("Tienes", hermanos, "en el centro")

salario=int(input("Introduce el salario familiar anual:"))
print("Salario familiar:", salario)
 
if distancia>=40 and hermanos>2 and salario>=20000:
	print("Puedes conseguir la beca")
else:
	print("No optas a beca")

##Haciendo más justo el programa

print(" ")
print("Vamos a evaluar las probabilidades de obtener la beca siendo más justos.")
 
if distancia>=40 and hermanos>2 or salario<=20000:
	print("Puedes conseguir la beca")
else:
	print("No optas a beca")

##Nuevo programa

print(" ")
nada=input("Pulsa para avanzar")


print("Aginaturas optativas 2020")
print("Opciones: Informática gráfica - Pruebas de Software - Dibujo Técnico")

opcion=input("Escribe la asignatura que prefieras:")
asignatura=opcion.lower()

#opcion.upper() #lo pone todo en mayus

if asignatura in ("informática gráfica", "pruebas de software", "dibujo técnico"):
	print("Asignatura elegida:" + asignatura)
else:
	print("La asignatura escogida no está disponible")


