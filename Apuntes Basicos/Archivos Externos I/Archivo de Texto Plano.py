from io import open


extxt = open("file.txt", "w")

text = "Learning Python \nI am liking it a lot!"

extxt.write(text)

extxt.close()

# --- LEEMOS EL CONTENIDO ---

extxt = open("file.txt", "r")

content = extxt.read()

extxt.close()

print(content)

# --- LEEMOS POR LINEAS ---

extxt = open("file.txt", "r")

lines = extxt.readlines()

extxt.close()

print(lines)

# Leer solo X linea

print(lines[1])

# --- AÑADIR INFORMACIÓN ---

extxt = open("file.txt", "a")

extxt.write("\nTy PildorasInformaticas")

extxt.close()
