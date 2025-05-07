from tkinter import *

## 함수 선언 부분 ##
def clickMouse(event):
    txt = ""
    if event.num == 1:
        txt += "마우스 왼쪽 버튼이 ("
    elif event.num == 3:
        txt += "마우스 오른쪽 버튼이 ("
    
    txt += str(event.y)+","+str(event.x)+")에서 클릭됨"
    label1.configure(text = txt)
    
## 메인 코드 부분 ##
window = Tk()
window.geometry("400x400")

label1 = Label(window, text="이곳이 바뀜")

window.bind("<Button>", clickMouse)

label1.pack(expand = 1, anchor = CENTER)
window.mainloop()
'''
4~12행 : 마우스 클릭할 때 실행될 이벤트 함수 선언
6~9행 : event.num 값은 마우스 왼쪽 버튼 클릭했을 때 1값을 가지고, 
        마우스 오른쪽 버튼을 클릭했을 때 3값 가짐
11행 : event.x와 event.y는 클릭한 위치의 좌표를 가짐
12행 : 18행에서 화면에 표시한 레이블의 글자 변경
20행 : 마우스 클릭하면 함수 호출
'''