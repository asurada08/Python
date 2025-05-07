from tkinter import *
window = Tk()

window.title("냥이들^^")
photo1 = PhotoImage(file="img/gif/cat.gif")
photo2 = PhotoImage(file="img/gif/cat2.gif")

label1 = Label(window, image=photo1)
label2 = Label(window, image=photo2)

label1.pack(side=LEFT) # 소문자로 쓰려면 'left' ''작은따옴표 써야함
label2.pack(side=RIGHT)

window.mainloop()