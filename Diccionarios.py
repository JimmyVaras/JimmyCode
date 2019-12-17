miDiccionario={"Alemania":"Berlín","Francia":"París", "España":"Madrid", "Irlanda":"Dublín"}

#Acceder a un valor asignado a un nombre o todo el diccionario.

print(miDiccionario["España"])
print(miDiccionario)

#Agregar más elementos

miDiccionario["Italia"]="Lisboa"
print(miDiccionario)

#Modificar valor de un nombre, se va a sobreescribir, es decir, no van a existir dos valores para un nombre

miDiccionario["Italia"]="Roma"
print(miDiccionario)

#Eliminar elemento, solo hace falta escribir la clave, no el valor

del miDiccionario["Francia"]
print(miDiccionario)

diccionarioEdades={"Jimmy":16, "Vega":14, "Nico":15}
print(diccionarioEdades)
print(diccionarioEdades["Nico"])
#Usando listas

ListaCities=["España","Francia", "Irlanda"]
diccionarioListado={ListaCities[0]:"Madrid",ListaCities[1]:"París",ListaCities[2]:"Dublín"}
print(diccionarioListado)

dictData={"Nombre":"Jimmy", "Edad":16, "Bach. Acabado":False, "LoL Years":[2016, 2017, 2018, 2019]}
print(dictData["Edad"])

#Pedir todas las claves del diccionario

print(dictData.keys())

#Pedir todos los valores

print(dictData.values())

#Pedir longitud del diccionario

print(len(dictData))
