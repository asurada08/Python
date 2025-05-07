from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def clickLeft(event):
    messagebox.showinfo("마우스", "마우스 왼쪽 버튼이 클릭됨")

## 메인 코드 부분 ##
window = Tk()

window.bind("<Button-1>", clickLeft)

window.mainloop()

'''
5~6행 : 마우스 이벤트가 발생할 때 작동할 함수 정의
11행 : window.bind() 함수에는 마우스 왼쪽 버튼 클릭할 때 발생하는 이벤트인
       <Button-1> 설정하고 5행의 clickLeft 함수명을 지정
'''