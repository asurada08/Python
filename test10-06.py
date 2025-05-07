from tkinter import *
from tkinter.filedialog import *

## 함수 선언 부분 ##
def func_open():
    filenames = askopenfilenames(parent = window, filetypes = (("gif파일","*.gif"),("모든파일","*.*")))
    if len(filenames) > 0:
        show_img(filenames)
    
def func_exit():
    window.quit()
    window.distroy()

def show_img(filenames):
    global photoList, num
    photoList = []
    num = 0
    
    for filename in filenames:
        photo = PhotoImage(file=filename)
        photoList.append(photo)
    
    # 첫번째 이미지 
    pLabel.configure(image=photoList[num])
    pLabel.image = photoList[num]

def clickNext():
    global photoList, num
    if num < len(photoList)-1:
        num += 1
        pLabel.configure(image=photoList[num])
        pLabel.image = photoList[num]
    
def clickPrev():
    global photoList, num
    if num > 0:
        num -= 1
        pLabel.configure(image=photoList[num])
        pLabel.image = photoList[num]
    
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

## 이전, 다음 버튼 부분
btnPrev = Button(window, text="이전", command = clickPrev)
btnPrev.pack(side='left', padx = 10, pady = 10)
btnNext = Button(window, text="다음", command = clickNext)
btnNext.pack(side='right', padx = 10, pady = 10)

window.mainloop()
