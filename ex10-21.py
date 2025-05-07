from tkinter import *
from tkinter.filedialog import *

## 함수 선언 부분 ##
window = Tk()
window.geometry("400x100")

label1 = Label(window, text="선택된 파일 이름")
label1.pack()

saveFp = asksaveasfile(parent = window, mode = "w", defaultextension=".jpg", filetypes = (("jpg파일","*.jpg"),("모든파일","*.*")))
                         
label1.configure(text = saveFp)
saveFp.close()

window.mainloop()
'''
11행 : asksaveasfile() 함수의 매개변수 중 mode="w"는 쓰기모드 라는 의미
       defaultextension=".jpg"는 특별히 확장명을 지정하지 않으면 확정명을 jpg로 붙인다는 의미
13행 : saveFp는 자체를 text에 대입시켜 출력
14행 : 파일 닫음
'''