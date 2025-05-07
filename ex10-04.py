from tkinter import *
window = Tk()

photo = PhotoImage(file="img/gif/dog.gif")
label1 = Label(window, image=photo)

label1.pack()

window.mainloop()