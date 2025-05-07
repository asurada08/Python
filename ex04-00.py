a=5; b=3
print(a+b, a-b, a*b, a/b, a//b, a%b, a**b)

a, b, c = 2, 3, 4
print(a+b-c, a+b*c, a*b/c)

s1, s2, s3 = "100", "100.123", "99999999999"
print(int(s1), float(s2)+1, int(s3)+1)

a=100; b=100.123
print(str(a) + "1", str(b)+"1")

a=10
a += 5; print(a)
a -= 5; print(a)
a *= 5; print(a)
a /= 5; print(a)
a //= 5; print(a)
a %= 5; print(a)
a **= 5; print(a)

a, b = 100, 200
print(a == b, a != b, a > b, a < b, a >= b, a <= b)

a = 99
print((a > 100) and (a < 200), (a > 100) or (a < 200), not(a ==100))

print(10&7, 123&456, 0xFFFF&0x0000)
print(10|7, 123|456, 0xFFFF|0x0000)
print(10^7, 123^456, 0xFFFF^0x0000)

a=12345
print(~a +1)

a=10
print(a << 1, a << 2, a << 3, a << 4)

a=10
print(a >> 1, a >> 2, a >> 3, a >> 4)

"""
jupyter notebook 에서
셀이 선택된 상태에서 a, b 셀 추가
셀이 선택된 상태에서 dd 셀 삭제
~ enter 셀 아래로 추가
^ enter 셀 실행
@ enter 셀 실행과 아래로 추가
!pip install 모듈 : 모듈 설치(!를 붙여야 콘솔창에서 입력하는것과 같은 역할함)
pip uninstall 모듈 : 모듈 제거
pip list : 설치된 모듈 확인
~ teb : 해당 함수에서 사용시에는 해당 함수 상세히 보기
^/ : 해당 줄에서 했을 때는 한줄 주석 지정/해제
\ : 한줄을 여러줄로 표현하기
''' ''' == """ """ : 여러줄 주석 또는 html의 <pre> 태그 기능

import keyword : keyword.kwlist : 예약어 확인
http://docs.python.org/ko/3/library/functions.html

파이썬의 자료형
수치 자료형      불(bool)자료형      군집 자료형(그룹자료형)
---------------------------------------------------------------
정수(int)        True, False         문자열(str), 리스트(list)
실수(float)                          튜플(tuple), 사전(dict)
복소수(complex):실수+허수            집합(set)
===============================================================
내장자료형 구분
분류 기준          종류
---------------------------------------------------------------
데이터 저장방법    직접표현(정수,실수등), 시퀀스(여러데이터,순서(O)),매핑(어려값,순서(X))
변경 가능성        변경가능, 변경불가능(튜플)
저장 개수          리터럴(한개 저장), 컨테이너(여러개 저장)
"""
