from tkinter import *

root = Tk()

root.title("Test Window")

root.resizable(0, 0)
root.iconbitmap("logo.ico")

root.geometry("950x600")

root.config(bg="white", relief="groove")

frame = Frame()
frame.pack(anchor="nw", fill="x")
frame.config(bg="black")
frame.config(width="400", height="44")
frame.config(relief="groove", bd="5")
frame.config(cursor="cross")

frame2 = Frame()

frame2.pack(anchor="sw")
frame2.config(bg="blue")
frame2.config(width="950", height="200")

label = Label(frame2, text="Texto dentro de una label dentro de un frame",
              fg="red", font=("Arial Black", 18))
label.pack()

# ==
# Label(frame2, text="Texto dentro de una label dentro de un frame").pack()
# ==

imagetwga = PhotoImage(file="twga.png")

Label(frame2, image=imagetwga).pack()



root.mainloop()
