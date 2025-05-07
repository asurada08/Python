from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def keyEvent(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키 : "+chr(event.keycode))

## 메인 코드 부분 ##
window = Tk()

window.bind("<Key>", keyEvent)
window.mainloop()
'''
5~6행 : 키보드가 눌릴 때 작동하는 함수 선언
        event.keycode에는 눌려진 키의 숫자 값 들어 있으므로 chr() 함수를
        사용하면 문자로 변환
11행 : <Key> 이벤트를 윈도우창에 사용
'''