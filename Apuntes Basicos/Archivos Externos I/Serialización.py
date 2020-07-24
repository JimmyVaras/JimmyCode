import pickle


list = ["Python", "HTML", "Ruby", "Java", "C"]

binaryfile = open("languajes", "wb")

pickle.dump(list, binaryfile)

binaryfile.close()

# Leemos el archivo

readingfile = open("languajes", "rb")

idiomas = pickle.load(readingfile)

print(idiomas)
