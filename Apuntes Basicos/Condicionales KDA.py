print("Bienvenido a la interfaz de evaluación de partidas 'KDAnivia'")

print("Las valoraciones van desde 'S' hasta 'D', siendo S la nota más alta ")

kills=input("Introduce el número de Kills: ")
deaths=input("Introduce el número de Muertes: ")
assist=input("Introduce el número de Asistencias: ")
cs=input("Introduce tu CS: ")
time=input("¿Cuanto ha durado la partida (solo los minutos): ")

kminusd=(int(kills))-(int(deaths))
kda=(kminusd)+((int(assist))*0.5)
cscore=(int(cs))/(int(time))
score=kda*(cscore/10)

print("Has matado a", int(cscore), "minions por minuto!")
print("Tu score a evaluar es de", int(score))

def eval(score):
	if score<0:
		valoración="D"
	elif score>8:
		valoración="S"
	elif score<8:
		valoración="A"
	elif score<6:
		valoración="B"
	elif score<3:
		valoración="C"
	else:
		valoración="D"

	return valoración

print(" ")
print(" ")
print("La valoración de tu partida es:", eval(score), "!")
