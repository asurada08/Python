import turtle
import random

## 클래스 선언 부분 ##
class Shape: # 슈퍼클래스
    myTurtle = None 
    cx, cy = 0, 0 # 도형의 중심점
    
    def __init__(self):
        self.myTurtle = turtle.Turtle("turtle") # 거북이 생성
    
    def setPen(self): # 펜 색상과 두께 무작위로 뽑기
        r = random.random()
        g = random.random()
        b = random.random()
        self.myTurtle.pencolor((r, g, b))
        pSize = random.randrange(1, 10)
        self.myTurtle.pensize(pSize)
    
    def drawShape(self): # 서브클래스에서 상속받아 오버라이딩
        pass
    
class Rectangle(Shape): # 서브클래스
    width, height = [0] * 2
    def __init__(self, x, y):
        Shape.__init__(self) # 슈퍼클래스의 생성자 호출
        self.cx = x
        self.cy = y
        self.width = random.randrange(20, 100)
        self.height = random.randrange(20, 100)
        
    def drawShape(self): # Overriding 재정의
        # 네모 그리기
        sx1, sy1, sx2, sy2 = [0] * 4 # 왼쪽 위 x, y 오른쪽 아래 x, y
        
        sx1 = self.cx - self.width / 2
        sy1 = self.cy - self.height / 2
        sx2 = self.cx + self.width / 2
        sy2 = self.cy + self.height / 2
        
        self.setPen() # 부모클래스 메서드
        self.myTurtle.penup()
        self.myTurtle.goto(sx1, sy1)
        self.myTurtle.pendown()
        self.myTurtle.goto(sx1, sy2)
        self.myTurtle.goto(sx2, sy2)
        self.myTurtle.goto(sx2, sy1)
        self.myTurtle.goto(sx1, sy1)

## 함수 선언 부분 ##
def screenLeftClick(x, y):
    rect = Rectangle(x, y)
    rect.drawShape()
    
## 메인 코드 부분 ##
turtle.title("거북이로 객체지향 사각형 그리기")
turtle.onscreenclick(screenLeftClick, 1)
turtle.done()
'''
5~21행 : 슈퍼 클래스인 도형(Shape) 클래스 선언
6~7행 : 도형에 공통으로 사용할 필드 준비
9~10행 : Shape 생성자에서 거북이 생성
12~18행 : 색상, 선 두께를 무작위 추출하는 메서드 선언
20행 : drawShape() 메서드는 서브 클래스에서 오버라이드
23~48행 : 서브클래스인 사각형(Rectangle)을 정의
24행 : Rectangle에서 필요한 속성인 폭과 넓이 준비
25~30행 : 사각형의 중심을 x, y로 받아 슈퍼클래스에서 상속받은 속성인 cx, cy에 대입
29~30행 : 사각형의 폭과 높이를 무작위로 추출
32~48행 : 슈퍼클래스의 drawShape() 메서드 오버라이드
36~39행 : 클릭한 점 중심으로 사각형의 왼쪽 위, 오른쪽 아래의 위치 계산
41~48행 : 사각형을 그림
51~53행 : 마우스 클릭 때마다 클릭 위치 이용 사각형 인스턴스 생성, drawShape()메서드 실행해서 사격형 그림
57행 : 마우스 클릭하면 screenLeftClick()메서드 실행하도록 설정
'''