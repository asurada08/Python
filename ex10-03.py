from tkinter import *
window = Tk()

label1= Label(window, text="COOKBOOK~~ Python을")
label2 = Label(window, text="열심히", font=("궁서체", 30), fg="blue")
label3 = Label(window, text="공부 중입니다", bg="magenta", width=20, height=5, anchor=SW)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()

'''
4행 : Label() 함수가 레이블을 만들어 줌
8행 : pack() 함수로 해당 레이블을 화면에 표시
Font : 글꼴과 크기 지정
fg : foreground의 약어 글자색 지정
bg : background의 약어 배경색 지정
width, height : 위젯의 폭과 높이를 지정
anchor : 위젯이 어느 위치에 자리 잡을지 결정
anchor : N, S, E, W, NE, SE, SW, NW, CENTER 기본값은 CENTER
label = (부모요소, 옵션)
label.pack() = 화면에 그리기
'''