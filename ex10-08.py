from tkinter import *
window = Tk()
window.geometry("300x300")

## 함수 선언 부분 ##
def myFunc():
    if var.get() == 1:
        ## 기존의 출력된 위젯의 모양을 변경할 때, 해당 위젯의 옵션 변경
        label1.configure(text="Python")
    elif var.get() == 2:
        label1.configure(text="C++")
    else:
        label1.configure(text="Java")
        
## 메인 코드 부분 ##
var = IntVar() ## 정수형 변수명 설정
rb1 = Radiobutton(window, text="Python", variable=var, value=1, command=myFunc)
rb2 = Radiobutton(window, text="C++", variable=var, value=2, command=myFunc)
rb3 = Radiobutton(window, text="Java", variable=var, value=3, command=myFunc)

label1 = Label(window, text="선택한 언어 :", fg="red")

rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()

window.mainloop()