from tkinter import *
from tkinter.filedialog import *

## 함수 선언 부분 ##
def func_open():
    filename = askopenfilename(parent = window, filetypes = (("gif파일","*.gif"),("모든파일","*.*")))
    photo = PhotoImage(file=filename)
    pLabel.configure(image = photo)
    pLabel.image = photo
    
def func_exit():
    window.quit()
    window.distroy()
    
## 메인 코드 부분 ##
window = Tk()
window.geometry("400x400")
window.title("명화 감상하기")

photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand = 1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command=func_exit)

window.mainloop()
'''
5~9행 : [파일열기] 메뉴를 선택하면 실행되는 함수 askopenfilename() 함수로
        파일 선택 후 선택한 파일명을 7행에서 PhotoImage()함수로 처리
8~9행 : 레이블에 이미지 표시
20~22행 : 선택한 gif 윈도우창에 출력하려고 레이블 준비
20행 : PhotoImage()에 별도의 매개변수 없이 빈 그림만 준비
'''