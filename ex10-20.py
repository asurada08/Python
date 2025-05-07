from tkinter import *
from tkinter.filedialog import *

## 함수 선언 부분 ##
window = Tk()
window.geometry("400x100")

label1 = Label(window, text="선택된 파일 이름")
label1.pack()

filename = askopenfilename(parent = window, filetypes=(("gif 파일","*.gif"),("모든파일","*.*")))

label1.configure(text = str(filename))

window.mainloop()
'''
11행 : askopenfilename() 함수 사용
13행 : filename 출력
'''