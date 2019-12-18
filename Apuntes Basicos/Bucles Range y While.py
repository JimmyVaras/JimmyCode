# Bucles usando el tipo range TODO

valido=True

email=input("Introduce tu email: ")

for i in range(len(email)):

    if email[i]=="@":

        valido = True

if valido==True:
    print(f"Tu correo es {email}")
else:
    print("Que te den")

# Bucle while
