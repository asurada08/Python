from tkinter import *

window = Tk()
window.title("윈도우 창 연습")
window.geometry("400x100+500+500") ## 가로x세로+x좌표+y좌표
window.resizable(width=False, height=False) ## 기본이 Ture 조절 가능 False 조절 불가

window.mainloop()