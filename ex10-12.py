from tkinter import *
from time import *

## 전역 변수 선언 부분 ##
fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif",
             "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]
phothList = [None] * 9
num = 0

## 함수 선언 부분 ##
def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    photo = PhotoImage(file="img/gif/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    
def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    photo = PhotoImage(file="img/gif/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo

## 메인 코드 부분 ##
window = Tk()
window.geometry("700x500")
window.title("사진 엘범 보기")

btnPrev = Button(window, text="<< 이전", command = clickPrev)
btnNext = Button(window, text="다음 >>", command = clickNext)

photo = PhotoImage(file="img/gif/"+fnameList[0])
pLabel = Label(window, image=photo)

btnPrev.place(x = 250, y = 10)
btnNext.place(x = 400, y = 10)
pLabel.place(x = 15, y = 50)

window.mainloop()

'''
5행 : fnameList 변수에 사진 9장 파일명 저장
7행 : photoList에는 PhotoImage() 함수로 생성할 변수 9개 준비
8행 : num은 현재 사진의 번호
11~18행 : <다음> 버튼을 누르면 실행되는 함수
12행 : global num은 num 전역 변수를 함수 안에서 사용 의미
13행 : 사진 번호를 하나 증가
14~15행 : 사진 번호가 최대 8, 8 넘으면 0번 사진 표시
16~18헹 : 변경된 사진 번호에 해당하는 이미지 파일로 pLabel 변경
20~27행 : <이전> 버튼을 누르면 처리되는 함수
34~35행 : 버튼 누르면 이 함수와 연결
37~38행 : 프로그램 실행 후 첫번째 사진 표시
40~42행 : 버튼 및 이미지 위치 place(x=좌표, y=좌표)로 지정
'''