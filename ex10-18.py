from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def func_open():
    messagebox.showinfo("메뉴선택", "열기 메뉴를 선택함")

def func_exit():
    window.quit()
    window.destroy()

## 메인 코드 부분 ##
window = Tk()

mainMenu = Menu(window)
window.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "종료", command=func_exit)

window.mainloop()
'''
5~6행 : [열기] 메뉴 선택하면 간단한 메시지창 열림
8~10행 : [종료] 메뉴 선택하면 프로그램 종료
20행 : command 값으로 func_open 함수 실행
22행 : command 값으로 func_exit 함수 실행
''' 
   