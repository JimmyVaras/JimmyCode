import datetime

meses = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto", \
9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"}

today = datetime.date.today()

print(f"Hoy es día {today.day} de {meses[(today.month)]} del año {today.year}")

cumple = datetime.date(2005, 5, 5)


print(f"Naciste el día {cumple.day} de {meses[(cumple.month)]} del año {cumple.year}.\n")


