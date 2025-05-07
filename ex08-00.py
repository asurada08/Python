## 문자열 기본
## 문자열 개념 : 리스트 코드와 비교
## list = [10, 20, 30, 40, 50]
aa = [10, 20, 30, 40, 50]
print("aa[0] :",aa[0])
print("aa[1:3] :",aa[1:3])
print("aa[3:] :",aa[3:])
## str = "파이썬수업"
ss = "파이썬수업"
print("ss[0] :", ss[0])
print("ss[1:3] :", ss[1:3])
print("ss[3:] :", ss[3:])
## +, * 기호 사용 문자열 반복
ss1 = '파이썬'+'수업'
print("ss1 :",ss1)
ss2 = '파이썬'*3
print("ss2 :",ss2)

'''
Function, Method 구분
str1 = "abcd"
len(str1) 이건 길이를 알아내는 Function
str1.upper() 이건 대문자로 바꾸는 Method
혼동하면 안됨
'''

## len()함수 : 리스트나 문자열의 개수를 셀때 사용
ss3 = '파이썬abc'
print("len(ss3) :",len(ss3))

## 대,소문자 변환 : upper(), lower(), swapcase(), title()
ss4 = "Python is Ease. 그래서 programming이 재미있습니다 ^^"
print("ss4.upper() :",ss4.upper())
print("ss4.lower() :", ss4.lower())
print("ss4.swapcase() :", ss4.swapcase())
print("ss4.title() :", ss4.title())

## 문자열 찾기 : count(), find(), rfind(), index(), rindex(), startswith(), endswith()
ss5 = "파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있지는 않죠^^"
## count() : 찾는 문자열의 개수
print("ss5.count('공부') :", ss5.count("공부")) ## 2
## find() : 찾는 문자열의 첫 인덱스, 왼쪽에서 부터 찾음
## rfind() : 찾는 문자열의 마지막 인덱스, 오른쪽에서 부터 찾음
print("ss5.find('공부') :", ss5.find("공부")) ## 4
print("ss5.rfind('공부') :", ss5.rfind("공부")) ## 21
print("ss5.find('공부',5) :", ss5.find('공부',5)) ## 21, (5번째 부터 찾아라)
print("ss5.find('없다') :", ss5.find("없다")) ## -1
## index() : find()와 같음, 지정된 문자열이 없으면 ValueError 오류 발생
## rindex() : rfind()와 같음
print("ss5.index('공부') :", ss5.index("공부")) ## 4
print("ss5.rindex('공부') :", ss5.rindex("공부")) ## 21
print("ss5.index('공부') :", ss5.index("공부",5)) ## 21, (5번째 부터 찾아라)
## startwith() 찾는 문자열이 시작하는 것이냐? 맞으면 True 아니면 False
## endwith() 찾는 문자열이 끝나는 문자열이냐? 맞으면 True 아니면 False
print("ss5.startswith('파이썬') :", ss5.startswith('파이썬')) ## T
print("ss5.startswith('파이썬',10) :", ss5.startswith('파이썬',10)) ## F
print("ss5.endswith('^^') :", ss5.endswith('^^')) ## T
## 문자열 공백 삭제,변경하기 : strip(), rstrip(), lstrip(), replace()
ss6 = "    파    이    썬    "
print("ss6.strip() :", ss6.strip()) ## 양쪽 공백 삭제
print("ss6.rstrip() :", ss6.rstrip()) ## 오른쪽 공백 삭제
print("ss6.lstrip() :", ss6.lstrip()) ## 왼쪽 공백 삭제
## 앞 뒤의 특정 문자 삭제
ss7 = "----파---이---썬----"
print("ss7 :",ss7)
print("ss7.strip('-') :", ss7.strip('-'))
ss8 = "<<파<<이>>썬>>"
print("ss8 :",ss8)
print("ss8.strip('<>') :", ss8.strip('<>'))
## 문자열 변경 replace()
ss9 = "열심히 파이썬 공부 중~~"
print("ss9 :",ss9)
print("ss9.replace('파이썬','Python') :", ss9.replace('파이썬','Python'))
## 문자열 분리, 결합하기 : split(), splitlines(), join()
ss10 = "Python을 열심히 공부 중"
print("ss10 :", ss10)
print("ss10.split(' ') :", ss10.split(' ')) ## ' '을 기준으로 분리
ss11= "Python을:열심히:공부:중"
print("ss11 :", ss11)
print("ss11.split(':') :", ss11.split(':')) ## ':'을 기준으로 분리
ss12 = "Python을\n열심히\n공부\n중"
print("ss12 :", ss12)
print("ss12.splitlines() :", ss12.splitlines()) ## '\n'을 기준으로 분리
ss13 = "$"
print("ss13 :", ss13)
print("ss13.join('파이썬') :", ss13.join("파이썬")) ## $이 구분자가 되어 파$이$썬 출력
## 함수명에 대입하기 : map()
before = ['2024','07','12']
after = list(map(int, before))
print("before :", before)
print("after :", after)
## 문자열 정렬하기, 채우기 : center(), ljust(), rjust(), zfill()
ss14 = "파이썬"
print("ss14 :", ss14)
print("ss14.center(10) :", ss14.center(10))
print("ss14.center(10,'*') :", ss14.center(10,'*'))
print("ss14.ljust(10) :", ss14.ljust(10))
print("ss14.rjust(10) :", ss14.rjust(10))
print("ss14.zfill(10) :", ss14.zfill(10))
'''
문자열 구성 파악하기
isdigit() : 문자열이 숫자로 이루어져 있는지 확인
isalpha() : 문자열이 알파벳으로 이루어져 있는지 확인
isalnum() : 문자열이 알파벳 or 숫자으로 이루어져 있는지 확인
islower() : 문자열이 소문자로 이루어져 있는지 확인
isupper() : 문자열이 대문자로 이루어져 있는지 확인
isspace() : 문자열이 공백으로 이루어져 있는지 확인
'''
print("'1234'.isdigit() :",'1234'.isdigit()) 
print("'abcd'.isalpha() :",'abcd'.isalpha())
print("'abc123'.isalnum() :",'abc123'.isalnum())
print("'abcd'.islower() :",'abcd'.islower())
print("'ABCD'.isupper() :",'ABCD'.isupper())
print("'    '.isspace() :",'    '.isspace())
