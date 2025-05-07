## 탭 메뉴 작성

from tkinter import *
from tkinter import ttk

'''
주요 ttk
Button :  기본 버튼 위젯
Label : 텍스트 또는 이미지를 표시하는 라벨
Entry : 단일 행 텍스트 입력 필드
Combobox : 드롭다운 목록
Treeview : 계층적 데이터를 표시하는 트리 구조
Notebook : 탭 인터페이스를 제공하는 위젯
Progressbar : 진행률 표시줄
Frame : 위젯을 그룹화 하고 레이아웃을 관리하기 쉽게 함
'''
win = Tk()

baseTab = ttk.Notebook(win) # 탭 인터페이스
tabDog = ttk.Frame(baseTab) # 강아지와 고양이를 그룹으로 만든다
baseTab.add(tabDog, text = "강아지") # 탭에 강아지 붙이기

tabCat = ttk.Frame(baseTab)
baseTab.add(tabCat, text = "고양이") # 탭에 고양이 붙이기

tabRabbit = ttk.Frame(baseTab)
baseTab.add(tabRabbit, text = "토끼") # 탭에 고양이 붙이기

baseTab.pack(expand = 1, fill = "both") # 탭 보이기, xy 채우기

photoDog = PhotoImage(file = "img/gif/dog5.gif")
labelDog = Label(tabDog, image = photoDog)
labelDog.pack()

photoCat = PhotoImage(file = "img/gif/cat5.gif")
labelCat = Label(tabCat, image = photoCat)
labelCat.pack()

photoRabbit = PhotoImage(file = "img/gif/rabbit2.gif")
labelRabbit = Label(tabRabbit, image = photoRabbit)
labelRabbit.pack()

win.mainloop()