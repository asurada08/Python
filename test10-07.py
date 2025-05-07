from tkinter import *
from tkinter.filedialog import *

## 함수 선언 부분 ##
def func_open():
    filename = askopenfilename(parent = window, filetypes = (("gif파일","*.gif"),("모든파일","*.*")))
    photo = PhotoImage(file=filename)
    
    ## 이미지 흑백으로 변경
    width = photo.width()
    height = photo.height()
    for i in range(height):
        for j in range(width):
            r, g, b = photo.get(j, i)
            gray = int((r+g+b)/3)
            
            #(r, g, b)컬러 이미지를 2자리 16진수형식으로 이미지 변환 / (i, j)는 좌표
            photo.put("#%02x%02x%02x" % (gray, gray, gray), (j, i))
    
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