def generaPares(limite):
    num = 1
    listapar = []
    while num < limite:
        listapar.append(num * 2)
        num += 1
    return listapar


print(generaPares(10))

# Generador


def generador(limit):

    num = 1

    while num < limit:

        yield num * 2

        num += 1


product = generador(30)

print(" ")
print(next(product))

print(" ")
print(next(product))

print(" ")
print(next(product))

print(" ")

# Yield from

def giveCity(*cuidades):
    for elemento in cuidades:
        #for subElemeto in elemento:
            yield from elemento

cuidadesGiven = giveCity("Madrid", "Barcelona", "Badajoz", "Cartagena")

print(next(cuidadesGiven))
print(next(cuidadesGiven))
