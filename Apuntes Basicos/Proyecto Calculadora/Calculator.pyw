from tkinter import *

root = Tk()

frame = Frame(root, bg="blue")
frame.pack()

root.config(bg="blue", relief="groove")

# Pantalla ----------------------

onscreen = StringVar()

screen = Entry(frame, textvariable=onscreen)
screen.grid(row=0, column=0, padx=3, pady=10, columnspan=4)
screen.config(bg="black", fg="#3bc319", justify="right")

# Pulsaciones


def pressed(num):
    onscreen.set(onscreen.get()+num)


# Fila 1 -------------------------

bot7 = Button(frame, text="7", width=3, command=lambda: pressed("7"))
bot7.grid(row="2", column="0")
bot8 = Button(frame, text="8", width=3, command=lambda: pressed("8"))
bot8.grid(row="2", column="1")
bot9 = Button(frame, text="9", width=3, command=lambda: pressed("9"))
bot9.grid(row="2", column="2")
botDiv = Button(frame, text="/", width=3)
botDiv.grid(row="2", column="3")

# Fila 2 -------------------------

bot4 = Button(frame, text="4", width=3, command=lambda: pressed("4"))
bot4.grid(row="3", column="0")
bot5 = Button(frame, text="5", width=3, command=lambda: pressed("5"))
bot5.grid(row="3", column="1")
bot6 = Button(frame, text="6", width=3, command=lambda: pressed("6"))
bot6.grid(row="3", column="2")
botMul = Button(frame, text="x", width=3)
botMul.grid(row="3", column="3")

# Fila 3 -------------------------

bot1 = Button(frame, text="1", width=3, command=lambda: pressed("1"))
bot1.grid(row="4", column="0")
bot2 = Button(frame, text="2", width=3, command=lambda: pressed("2"))
bot2.grid(row="4", column="1")
bot3 = Button(frame, text="3", width=3, command=lambda: pressed("3"))
bot3.grid(row="4", column="2")
botRes = Button(frame, text="-", width=3)
botRes.grid(row="4", column="3")

# Fila 4 -------------------------

bot0 = Button(frame, text="0", width=3, command=lambda: pressed("0"))
bot0.grid(row="5", column="0")
botcoma = Button(frame, text=",", width=3, command=lambda: pressed(","))
botcoma.grid(row="5", column="1")
botigual = Button(frame, text="=", width=3)
botigual.grid(row="5", column="2")
botSum = Button(frame, text="+", width=3)
botSum.grid(row="5", column="3")


root.mainloop()
