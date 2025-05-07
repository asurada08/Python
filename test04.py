"""
연습문제1)
출력형식
연도를 입력하세요 : 2024
2024년은 윤년입니다

아닐경우는
연도를 입력하세요 : 2023
2023년은 윤년이 아닙니다
"""
if __name__ == "__main__":
    year = int(input("연도를 입력하세요 : "))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year,"년은 윤년입니다")
        print(__name__)
    else:
        print("%d 년은 윤년이 아닙니다" % year)
        print(__name__)
else:
    print(__name__)

"""
연습문제2)
거북이로 2진수를 표현하세요
빨간 거북이는 1 파란거북이는 0
"""
import turtle

## 전역 변수 선언 부분 ##
num = 0
swidth, sheight = 1000, 300
curX, curY = 0, 0

## 메인 코드 부분 ##
if __name__ == "__main__":
    turtle.title("거북이로 2진수 표현하기")
    turtle.shape("turtle")
    turtle.setup(width = swidth+50, height = sheight+50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.left(90)

    num=int(input("숫자를 입력하세요 : "))
    binary = bin(num) ##bin(10) == 0b1010
    curX = swidth / 2
    curY = 0
    for i in range(len(binary)-2):
        turtle.goto(curX, curY)
        if num & 1:
            turtle.color("red")
            turtle.turtlesize(2) ## 그리기 붓 크기
        else:
            turtle.color("green")
            turtle.turtlesize(1)
        turtle.stamp() ## 붓 모양 찍기
        curX -= 50 ## 찍히는 위치 이동
        num >>= 1 ## 시프트 연산

turtle.done()
    
