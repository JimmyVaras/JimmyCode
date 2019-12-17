miTupla=("Jimmy", 5, 5, 2003)

print(miTupla[2])
	
#Convertir tupla en lista

miLista=list(miTupla)

print(miLista)

#Convertir lista a tupla

otraTupla=tuple(miLista)

print(otraTupla)

#Comprobar si existe un elemento

print("Jimmy" in miTupla)
print(4 in miTupla)

#Contar elementos de una tupla ¡

print(miTupla.count("Jimmy"))
print(miTupla.count(5))

#Número de elementos de en la tupla

print(len(miTupla))

#Tuplas unitarias

unitaria=("Anivia",)
print(len(unitaria))

#Tuplas sin paréntesis

noparentesis="Ryze", 2, 3, 6
print(noparentesis)

#Declarar valores de la tupla a unas variables

nombre, dia, mes, año=miTupla

#Desempaquetado de tuplas

print(nombre)
print(dia)
print(mes)
print(año)

 