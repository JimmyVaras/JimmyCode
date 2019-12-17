#Bucles For 

for i in [1,2,3]:
	print("Hola!", end=" ")

for i in ["Invierno","Primavera","Verano"]:
 	print(i)

#Bucles tipo Range

for i in "Jimmy":
	print("ha", end="")

print(" ")

#Test e-mail

correo=input("Introduce tu correo electrónico: ")
email=False

for i in correo:
	if(i=="@"):
 		email=True

if email==True: #if email: (tb sirve)
	print("Tu correo es correcto")
else:
	print("No correcto")

#

for i in range (5):
	print(i)


