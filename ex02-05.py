import turtle

## 함수 선언부분 ##


## 변수 선언 부분 ##
myT=None

## 메인 코드 부분 ##
'''
turtle.shape('turtle')

turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)

turtle.done()
'''
myT=turtle.Turtle()
myT.shape('turtle')

for i in range(0, 4):
    myT.forward(200)
    myT.right(90)

turtle.done()
