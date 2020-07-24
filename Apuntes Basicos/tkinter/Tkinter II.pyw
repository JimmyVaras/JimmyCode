from tkinter import *


root = Tk()


frame1 = Frame(root, width=1280, height="720")
frame1.pack()

name = StringVar()

textinput1 = Entry(frame1, textvariable=name)
textinput1.grid(row=0, column=1)
textinput1.config(fg="blue", justify="left")

textinput2 = Entry(frame1)
textinput2.grid(row=1, column=1)
textinput1.config(fg="blue", justify="right")

textinput3 = Entry(frame1)
textinput3.grid(row=2, column=1)
textinput1.config(fg="blue", justify="center")

label1 = Label(frame1, text="Nombre: ")
label1.grid(row="0", column="0", sticky="e", pady="3", padx="5")

label2 = Label(frame1, text="Apellido: ")
label2.grid(row="1", column="0", sticky="e", pady="3", padx="5")

label3 = Label(frame1, text="Edad: ")
label3.grid(row="2", column="0", sticky="e", pady="3", padx="5")

textinputp = Entry(frame1)
textinputp.grid(row=3, column=1)
textinputp.config(fg="black", justify="center", show="●")

labelp = Label(frame1, text="Contraseña: ")
labelp.grid(row="3", column="0", sticky="e", pady="7", padx="10")

labelh = Label(frame1, text="Historia: ")
labelh.grid(row="4", column="0", sticky="e")

texthistoria = Text(frame1, width=15, height=10)
texthistoria.grid(row="4", column="1")

scroolVert = Scrollbar(frame1, command=texthistoria.yview)
scroolVert.grid(row="4", column="2", sticky="nsew")
texthistoria.config(yscrollcommand=scroolVert.set)


def savebuttoncode():

    name.set("Jimmy")


savebutton = Button(root, text="Guardar", command=savebuttoncode)
savebutton.pack()


root.mainloop()
