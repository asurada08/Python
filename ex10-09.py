from tkinter import *
window = Tk()

button1 = Button(window, text="버튼1")
button2 = Button(window, text="버튼2")
button3 = Button(window, text="버튼3")

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)

window.mainloop()

'''
button1.pack(side=LEFT)
side=LEFT : 옵션은 왼쪽부터 채우라는 의미
'''