from tkinter import *

window = Tk()

mainMenu = Menu(window)
window.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "열기")
fileMenu.add_separator()
fileMenu.add_command(label = "종료")

editMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "편집", menu = editMenu)
editMenu.add_command(label = "잘라내기")
editMenu.add_command(label = "복사")
editMenu.add_command(label = "붙여넣기")

window.mainloop()
'''
5행 : Menu(부모윈도우)로 mainMenu변수 생성 
      mainMenu 메뉴 자체를 나타내는 변수
6행 : 생성한 메뉴 자체를 윈도우차으이 메뉴로 지정
8~9행 : 상위 메뉴인 [파일] 생성, 메뉴 자체에 부착 [파일] 메뉴는
        선책하고 끝나는 것이 아니라, 그 아래에 다른 메뉴가 확장되어야 하므로,
        add_cascade()함수 사용
10행 : [파일]메뉴의 하위에 [열기]메뉴 준비, 선택할 때 어떤 작동을 해야하므로,
       add_command()함수 사용
11행 : 메뉴 사이에 구분선
12행 : 같은 방식으로 하위 메뉴 생성
14~18행 : [편집] 메뉴 추가, 하위 메뉴에 잘라내기, 복사, 붙여넣기 추가 실행은 안됨.
'''