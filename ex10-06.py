## 이미지 버튼을 누르면 간단한 메시지창이 나오는 코드
from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def myFunc():
    messagebox.showinfo("강아지 버튼", "강아지가 귀엽죠? ^^")

## 메인 코드 부분 ##
window = Tk()

photo = PhotoImage(file="img/gif/dog2.gif")
button1 = Button(window, image = photo, command=myFunc)

button1.pack()

window.mainloop()
'''
2행 : messagebox 모듈 사용 임포트
5~6행 : myFunc() 함수 정의, 이 함수는 messagebox.showinfo(제목, 내용)
        형식으로 화면에 메시지 상자 출력
11~12행 : 이미지 준비하고 버튼에 글자 대신 이미지 표현
'''