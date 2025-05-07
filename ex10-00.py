## 기본 윈도우창의 구성
## 위젯(Widget) : 윈도우창에 나올 수 있는 문자, 버튼, 체크박스, 라디오버튼 등을 의미

## 레이블(Label) : 문자를 표현할 수 있는 위젯

## 레이블에 글자 대신 이미지 넣기 : PhotoImage()는 GIF 파일만 지원, JPEG나 BMP 등은 지원하지 않음
## 위젯을 가로로 나타내려면 pack(side=LEFT), pack(side=RIGHT) 사용

## 버튼(Button) : 마우스로 클릭하면 눌리는 효과와 함께 지정한 작업 실행
## ex10-05.py : 버튼을 누르면 파이썬 IDLE이 종료되는 코드

## 체크버튼(Checkbutton) : 켜고 끄는데 사용하는 위젯
## ex10-06.py : 체크버튼을 켜거나 끄면 메시지창이 열리게 하는 코드

## 라디오버튼(Radiobutton) : 여러 개 중에서 하나를 선택하는데 사용하는 위젯

## 위젯의 배치와 크기 조절
## 수평 정렬 : pack() 함수 옵션 side = LEFT, RIGHT, 'left', 'right'
## 수직 정렬 : pack() 함수 옵션 side = TOP, BOTTOM, 'top', 'bottom'
## 폭 조정 : pack() 함수 옵션 윈도우창 폭에 맞추는 방법 fill = X
## 위젯 사이 여백조절 : pack() 함수 옵션 padx = 픽셀값, pady = 픽셀값
## 위젯 내부 여백조절 : pack() 함수 옵션 ipadx = 픽셀값, ipady = 픽셀값

## 고정 위치에 배치 : pack() 대신 place() 함수 사용

## configure Mathod : widget.configure(option=value, ...)
'''
configure(option=value) option
    text : Label, Button 등에서 텍스트 내용 설정
    fg : 텍스트나 요소의 색을 설정
    bg : 요소의 배경색을 설정
    font : 텍스트의 글꼴
    image : Label 등에 이미지 설정
    command : Button의 클릭 이벤트를 처리할 함수 설정
    width, height : 위젯의 너비 높이 설정
'''

## 마우스 이벤트
'''
클릭할 때 : <Button>(모든버튼 공통), <Button-1>(왼쪽버튼), <Button-2>(가운데버튼) <Button-3>(오른쪽버튼)
때었을 때 : <ButtonRelease>(모든버튼 공통), 나머지 위와 동일
더블 클릭 : <Double-Button>(모든버튼 공통), 나머지 위와 동일
드래그 시 : <B1-Motion>(왼쪽), <B2-Motion>(가운데), <B3-Motion>(오른쪽)
마우스 커서가 위젯 위로 올라왔을때 : <Enter>
마우스 커서가 위젯에서 떠났을때 : <Leave>
'''
## 마우스 이벤트 처리 형식
'''
def 이벤트처리함수(event):
    # 마우스 이벤트가 발생할 때 작동할 내용
위젯.bind("마우스이벤트", 이벤트처리함수)
'''
## 키보드 이벤트
'''
모든 키를 누를 때 : <Key>
특수 키를 누를 때 : <Return>, <BackSpace>, <Tap>, <Shift_L>, <Alt_L>, <Pause>,
                   <Caps_Lock>, <Escape>, <End>, <Home>, <Left>, <Right>, <Up>,
                   <Down>, <Num_Lock>, <Delete>, <F1>~<F12> 등
일반 키를 누를 때 : a~z, A~Z, 0~9, <Space>, <less>
화살표 키와 조합 : <Shift-Up>, <Shift-Down>, <Shift-Left>, <Shift-Right> 등
Enter를 처리하려면 <Key> 대신 <Return>을 사용
대, 소문자 등도 구분해서 처리 가능
일반 키를 누를 때 주의할 점은 SpaceBar는 <Space>로 <는 <less>로 사용
'''

## 메뉴와 대화상자
'''
메뉴의 생성 : 메뉴의 구성 개념과 형식
상위메뉴 ─┬─ 하위메뉴1
          └─ 하위메뉴2

메뉴자체 = Meun(부모윈도우)
부모윈도우.config(menu = 메뉴자체)

상위메뉴 = Meun(메뉴자체)
메뉴자체.add_cascade(label="상위메뉴텍스트", meun=상위메뉴)
상위메뉴.add_commaned(label="하위메뉴1", command=함수1)
상위메뉴.add_commaned(label="하위메뉴2", command=함수2)
'''