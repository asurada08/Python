from tkinter import *
from tkinter.simpledialog import *

## 함수 선언 부분 ##
window = Tk()
window.geometry("400x100")

label1 = Label(window, text="입력된 값")
label1.pack()

value = askinteger("확대배수", "주사위 숫자(1~6)을 입력하세요", minvalue=1, maxvalue=6)

label1.configure(text=str(value))
window.mainloop()
'''
8~9행 : 레이블 하나 준비
11행 : askinteger("제목","내용",옵션) 함수로 정수 입력
13행 : 입력받은 숫자를 문자열로 변경해서 레이블에 씀
'''