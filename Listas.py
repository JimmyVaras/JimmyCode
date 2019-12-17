listaPets=["Dog", "Cat", "Fish"]

#Imprimir entera la lista

print(listaPets)
print(listaPets[:])

#Imprimir un valor, se cuenta desde 0, este incluído.

print(listaPets[0])
print(listaPets[2])

#Se puede empezar por detrás de la lista, usando números negativos

print(listaPets[-1])

#Imprimir porción de la lista, queda excluído el último. Se puede no poner el 0 si quieres empezar desde el principio
#También se puede hacer al revés, para que llegue hasta el final.


print(listaPets[0:2])
print(listaPets[:2])
print(listaPets[1:])

#Añadir un nuevo valor a la lista al final

listaPets.append("Hamster")

#Añadir en una posición concreta

listaPets.insert(2, "Parrot")

print(listaPets)

#Añadir varios elementos a la lista

listaPets.extend(["Lizard","Rabbit"])

print(listaPets)

#Obtener la posición de un elemento en la lista

print(listaPets.index("Fish"))

#Comprobar si un elemento existe en la lista, devuelve True o False

print("Parrot" in listaPets)
print("Lion" in listaPets)

#Lista con diferentes tipos de valores

listaMixta=["Jimmy", 5, 3.31, True]

#Eliminar elementos de una lista

listaPets.remove("Lizard")
print(listaPets)

#Eliminar el último elemento de una lista

listaPets.pop()
print(listaPets)

#Sumar listas

listaSuma=listaPets+listaMixta

print(listaSuma)

#Multiplicar listas

listaMultiplicada=listaPets*3

print(listaMultiplicada)

print(listaPets*3) 
