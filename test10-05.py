from tkinter import *
from tkinter.filedialog import *

## 함수 선언 부분 ##
window = Tk()
window.geometry("500x500")

label1 = Label(window, text="선택된 파일 이름")
label1.pack(expand=1)

filename = askopenfilename(parent = window, filetypes=(("gif 파일","*.gif"),("모든파일","*.*")))
photo = PhotoImage(file=filename)

label1.configure(image = photo)

window.mainloop()
'''
ex10-20.py에 이름만 불러오는걸 사진을 불러오는걸로 수정
'''