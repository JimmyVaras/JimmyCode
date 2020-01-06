import random
import math

inv1 = str(input("¿Cual va a ser tu primer objeto? Escribelo: "))
inv2 = str(input("Introduce tu segundo objeto: "))
inv3 = str(input("Escribe tu tercer y último objeto: "))

print(f"Empiezas la aventura con {inv1}, {inv2} y {inv3}. Suerte!")

input("Enter para continuar")

trist = 0
chung = 0

def dado():
	resul = random.randint(1,6)
	return resul

print("Cada ve que quieras lanzar el dado escribe dado.")
print("Si quieres intercambiar un objeto escribe el numero del slot donde lo quieres colocar: 1, 2 o 3.")
print("Para aumentar en 1 la tristeza escribe 'trist' y para la chungez 'chung'. ")
print("Para ver tu inventario escribe 'inventario'. ")
print("Para ver tus estadisticas escribe 'stats'. ")
print("Para empezar un enfrentamiento escribe 'batalla' ")
def prop(com):
	global inv1
	global inv2
	global inv3
	global trist
	global chung
	if com == "1":
		inv1 = str(input(f"Escribe el nuevo objeto para sustituir a tu {inv1}: "))
	if com == "2":
		inv2 = str(input(f"Escribe el nuevo objeto para sustituir a tu {inv2}: "))
	if com == "3":
		inv3 = str(input(f"Escribe el nuevo objeto para sustituir a tu {inv3}: "))	
	if com == "dado":
		print(dado())		
	if com == "batalla":
		enemigo = int(input("Introduce las tiradas del enemigo: "))
		dp1 = random.randint(1,6)
		dp2 = random.randint(1,6)
		ptsdp = dp1 + dp2
		print(f"Has sacado {ptsdp}.")
		ene = []
		for i in range (enemigo):
			ene.append(random.randint(1,6))
		print("El enemigo ha obtenido", sum(ene))
		if sum(ene) > ptsdp:
			print("El enemigo gana el enfretamiento")
		else:
			print("Ganas el enfretamiento")
	if com == "stats":
		print(f"Tu puntos de Tristeza actuales son {trist} y tienes {chung} puntos de chunguéz.")		
	if com == "trist":
		trist+= 1
		print(f"Tu tristeza esta en {trist}.")
	if com == "chung":
		chung+= 1
		print(f"Tu chunguéz esta en {chung}.")
	else:
		print("Acción inexistente, intentalo de nuevo.")
	
		
while True:	
	prop(str(input("Que quieres hacer? -")))
