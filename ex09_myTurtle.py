import random
from tkinter.simpledialog import *

def getString(): # 문자열을 입력받아 반환하는 함수
    retStr = ""
    retStr = askstring("문자열 입력", "거북이 쓸 문자열을 입력")
    return retStr

def getRGB(): # 무작위로 RGB 색상 추출해서 튜플 반환하는 함수
    r, g, b = 0, 0, 0
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

def getXYAS(sw, sh): # x, y, 각도, 크기를 무작위로 추출해서 리스트로 묶어 반환하는 함수
    x, y, angel, size = 0, 0, 0, 0
    x = random.randrange(int(-sw / 2), int(sw / 2))
    y = random.randrange(int(-sh / 2), int(sh / 2))
    angel = random.randrange(0, 360)
    size = random.randrange(10, 50)
    return [x, y, angel, size]
