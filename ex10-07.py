from tkinter import *
from tkinter import messagebox
window = Tk()

## 함수 선언 부분 ##
def myFunc():
    if chk.get() == 0:
        messagebox.showinfo("","체크버튼이 꺼졌어요.")
    else:
        messagebox.showinfo("","체크버튼이 켜졌어요.")

## 메인 코드 부분 ##
chk = IntVar()
cd1 = Checkbutton(window, text = "클릭하세요", variable=chk, command=myFunc)

cd1.pack()

window.mainloop()

'''
6~10행 : myFunc()함수는 chk.get()함수, 체크버튼에 설정된 값을 가져와서 메시지 출력
13행 : chk 변수를 준비, IntVar()함수 사용
14행 : Checkbutton()의 옵션 중 variable에 chk 변수 사용
IntVar(): integer(정수) 변수를 선언
'''