import random
import pickle
import time
import os
import os.path
import webbrowser


def createdata():
  nuevos = []
  uno = str(input("¿Cual va a ser tu primer objeto? Escribelo: "))
  nuevos.append(uno)
  dos = str(input("Introduce tu segundo objeto: "))
  nuevos.append(dos)
  tres = str(input("Escribe tu tercer y último objeto: "))
  nuevos.append(tres)
  data = open("data","wb")
  pickle.dump(nuevos,data)
  data.close()

try:
  data = open("data","rb")
  saved = pickle.load(data)
  data.close()
except:
  createdata()

# ------ Importamos data -----------

data = open("data","rb")
saved = pickle.load(data)

inv1 = saved[0]
inv2 = saved[1]
inv3 = saved[2]
nuevos=[inv1,inv2,inv3]
try:
	trist = saved[3]
	chung = saved[4]
except:
	trist = 0
	chung = 0

data.close()

# *-*-*-*-*-*-**-*-*-*-*-*-* Cuerpo del programa *-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*

print(f"Empiezas la aventura con {saved[0]}, {saved[1]} y {saved[2]}. Suerte!")

input("-----Enter para continuar-----\n")

def dado():
	resul = random.randint(1,6)
	return resul

# ---------------- INSTRUCCIONES ----------------------

print("Cada ve que quieras lanzar el dado escribe 'dado'.")
print("Si quieres intercambiar un obsavedjeto escribe el numero del slot donde lo quieres colocar: 1, 2 o 3.")
print("Para aumentar en 1 la tristeza escribe 'trist' y para la chungez 'chung'. ")
print("Para ver tu inventario escribe 'inventario'. ")
print("Para ver tus estadisticas escribe 'stats'. ")
print("Para empezar un enfrentamiento escribe 'batalla'. ")
print("Escribe 'borrar' si deseas eliminar los datos guardados.")
print("Para finalizar el programa usa: 'end'.\n ")

# -------------- Comando principal ---------------------

def prop(com):
	global inv1
	global inv2
	global inv3
	global trist
	global chung
	global data

	if com == "1":
		inv1 = str(input(f"Escribe el nuevo objeto para sustituir a tu {inv1}: "))
	elif com == "2":
		inv2 = str(input(f"Escribe el nuevo objeto para sustituir a tu {inv2}: "))
	elif com == "3":
		inv3 = str(input(f"Escribe el nuevo objeto para sustituir a tu {inv3}: "))	

	elif com == "inventario":
		print(f"Ahora mismo llevas:\n-{saved[0]} \n-{saved[1]} \n-{saved[2]}\n!Suerte!")

	elif com == "dado":
		print(dado())	

	elif com == "batalla":
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
			print("El enemigo gana el enfretamiento\n")
		else:
			print("Ganas el enfretamiento\n")
			
	elif com == "stats":
		print(f"Tu puntos de Tristeza actuales son {trist} y tienes {chung} puntos de chunguéz.\n")	

	elif com == "trist":
		trist+= 1
		print(f"Tu tristeza esta en {trist}.")

	elif com == "chung":
		chung+= 1
		print(f"Tu chunguéz esta en {chung}.")

	elif com == "end":
		nuevos = [inv1,inv2,inv3,trist,chung] 
		data = open("data","wb")
		pickle.dump(nuevos,data)
		data.close()
		print("Programa creado por Jaime Varas \n-TW: @JimmyDaBlue \n-GitHub: github.com/JimmyVaras\
		 \n______Gracias por usarlo______\n© DeadTool v2.3 , JimmyVaras \nCopyright (c) 2019 JimmyVaras \nAll Rights Reserved\n")
		time.sleep(0.75)
		print("Se han guardado tus datos, programa finalizado")
		time.sleep(1)
		webbrowser.open("https://twitter.com/JimmyDaBlue", new=1, autoraise=True)
		time.sleep(0.5)

		quit()

	elif com == "borrar":
		data.close()
		dir_path = os.path.dirname(os.path.realpath(__file__))
		os.remove(f"{dir_path}/data")
		print("Se han borrado todos los datos anteriores\n")
		createdata()

	else:
		print("Acción inexistente, intentalo de nuevo.\n")

# ------ Bucle Principal LOOP -----------

while True:	
	prop(str(input("Que quieres hacer? -")))


# Programa creado por Jaime Varas -TW: @JimmyDaBlue -GitHub: github.com/JimmyVaras
# Gracias por usarlo
# © DeadTool , JimmyVaras
#
#Copyright (c) 2019 JimmyVaras
#All Rights Reserved
 
#This product is protected by copyright and distributed under
#licenses restricting copying, distribution, and decompilation.

