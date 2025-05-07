from tkinter import *
window = Tk()
window.geometry("300x300")

btnList = [None] * 3 ## == [""] * 3

for i in range(0, 3):
    btnList[i] = Button(window, text = "버튼"+str(i+1))
'''
for btn in btnList:
    btn.pack(side=RIGHT)
'''
'''
for btn in btnList:
    btn.pack(side = TOP, fill = X, padx = 10, pady = 10)
'''
'''
for btn in btnList:
    btn.pack(side = BOTTOM, fill = X, ipadx = 10, ipady = 10)
'''

for btn in btnList:
    btn.pack(side = BOTTOM, fill = X, ipadx = 10, ipady = 10, padx = 10, pady = 10)

window.mainloop()
'''
4행 : 비어있는 리스트를 3개 준비
6~7행 : 3회 반복하면서 버튼 생성
9~10행 : 준비한 버튼 리스트를 화면에 출력
13~14행 : 수직정렬 TOP는 위에서 부터 순서대로 BOTTOM은 밑에서부터 순서대로
        : fill = X 윈도우창 폭에 맞추는 방법, Y는 높이에 맞추는 방법
        : padx = 픽셀값, pady = 픽셀값 위젯 사이에 여백을 줌
17~18행 : ipadx = 픽셀값, ipady = 픽셀값 위젯 내부에 여백을 줌
20~21행 : 위젯 내부와 외부에 모두 여백
'''