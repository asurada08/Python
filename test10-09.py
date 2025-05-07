from tkinter import *

## 함수 선언 부분 ##
def show_img():
    if var.get() == 1:
        photo = PhotoImage(file="img/gif/cat.gif")
        label1.configure(image=photo)
        label1.image = photo
    elif var.get() == 2:
        photo = PhotoImage(file="img/gif/dog.gif")
        label1.configure(image=photo)
        label1.image = photo
    elif var.get() == 3:
        photo = PhotoImage(file="img/gif/rabbit.gif")
        label1.configure(image=photo)
        label1.image = photo

## 메인 코드 부분 ##
if __name__ == "__main__":
    win = Tk()
    win.geometry("300x500")
    win.title("애완동물 선택하기")

    var = IntVar()
    vLabel = Label(win, text = "좋아하는 동물 투표", font=("굴림", 20, "bold"), fg="green")
    rb1 = Radiobutton(win, text="고양이", variable=var, value=1)
    rb2 = Radiobutton(win, text="강아지", variable=var, value=2)
    rb3 = Radiobutton(win, text="토끼", variable=var, value=3)
    btn = Button(win, text = "사진 보기", command=show_img)

    photo = PhotoImage()
    label1 = Label(win, image = photo)

    vLabel.pack(padx=10, pady=10)
    rb1.pack(padx=10, pady=10)
    rb2.pack(padx=10, pady=10)
    rb3.pack(padx=10, pady=10)
    btn.pack(padx=10, pady=10)
    label1.pack(padx=10, pady=10)

    win.mainloop()


## 모범답안?
'''
## 함수 선언 
def myFunc():
    if var.get() == 1:
        labelImage.configure(image = photo1)
    elif var.get() == 2:
        labelImage.configure(image = photo2)
    else:
        labelImage.configure(image = photo3)
## 전역 변수 선언
var, labelImage = 0, None
photo1, photo2, photo3 = [None] * 3
## 메인 코드 작성
if __name__ == "__main__":
    window = Tk()
    window.geometry("400x400")
    window.title("애완동물 선택하기")
    labelText = Label(window, text = "좋아하는 동물 투표", fg = "blue", font = ("궁서체", 20))
    
    var = IntVar()
    rb1 = Radiobutton(window, text="고양이", variable=var, value=1)
    rb2 = Radiobutton(window, text="강아지", variable=var, value=2)
    rb3 = Radiobutton(window, text="토끼", variable=var, value=3)
    btn = Button(window, text = "사진 보기", command=myFunc)
    
    photo1 = PhotoImage(file="img/gif/cat.gif")
    photo2 = PhotoImage(file="img/gif/dog.gif")
    photo3 = PhotoImage(file="img/gif/rabbit.gif")
    
    labelImage = Label(window, width = 200, height = 200, bg = "yellow", image = None )
    
    labelText.pack(padx=5, pady=5)
    rb1.pack(padx=5, pady=5)
    rb2.pack(padx=5, pady=5)
    rb3.pack(padx=5, pady=5)
    btn.pack(padx=5, pady=5)
    labelImage.pack(padx=5, pady=5)
## 루핑
window.mainloop()
'''