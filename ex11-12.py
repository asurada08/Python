from tkinter import *

## 함수 선언 부분 ##
def loadImage(fname):
    global inImage, XSIZE, YSIZE
    fp = open(fname, 'rb')
    
    for i in range(0, XSIZE):
        tmpList = []
        for k in range(0, YSIZE):
            data = int(ord(fp.read(1)))
            tmpList.append(data)
        inImage.append(tmpList)
    
    fp.close()

def displayImage(image):
    global XSIZE, YSIZE
    rgbString = ""
    for i in range(0, XSIZE):
        tmpString = ""
        for k in range(0, YSIZE):
            data = image[i][k]
            tmpString += "#%02x%02x%02x " % (data, data, data) # "#%02x%02x%02x " 끝에 띄우쓰기
        rgbString += "{"+tmpString+"} " # "{"+tmpString+"} " 끝에 띄워쓰기
        print(rgbString, "-----------")
    paper.put(rgbString)

## 전역 변수 선언 부분 ##
window = None
canvas = None
XSIZE, YSIZE = 256, 256
inImage = [] # 2차원 리스트(메모리)

## 메인 코드 부분 ##
window = Tk()
window.title("흑백 사진 보기")
canvas = Canvas(window, height = XSIZE, width = YSIZE)
paper = PhotoImage(width = XSIZE, height = YSIZE)
canvas.create_image((XSIZE / 2, YSIZE / 2), image = paper, state = "normal")

# 파일 -> 메모리
filename = 'img/RAW/tree.raw'
loadImage(filename)

# 메모리 -> 화면
displayImage(inImage)

canvas.pack()
window.mainloop()
'''
30~33행 : 관련 변수 준비
43행 : 파일명 지정
44행 : loadImage()함수에 파일명 전달해 해당 파일을 inImage 리스트에 불러들임
47행 : displayImage() 함수에 inImage 리스트를 전달해 윈도우 창에 출력
'''