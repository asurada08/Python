## 파일 입출력
'''
파일 입출력 개념 : 표준 입출력과 파일 입출력 함수
입력 관련 : input()
출력 관련 : print()
파일 입력 관련 : read(), readline(), readlines()
파일 출력 관련 : write(), writelines()
'''
## 파일 입출력 기본 과정 : 파일열기 -> 파일읽기/파일쓰기 -> 파일닫기
## 파일열기 : (읽기용) 변수명 = open("파일명", "r"), (쓰기용) 변수명 = open("파일명", "w")
## 파일닫기 : 변수명.close()
## 파일열기모드
'''
open() 함수 매개변수
r : 읽기 모드, 기본값 / w : 쓰기 모드, 기존에 파일이 있으면 덮어쓴다
r+ : 읽기 / 쓰기 겸용모드 / a : 쓰기 모드, 기존에 파일이 있으면 이어서 씀(append약어)
t : 텍스트 모드, 텍스트 파일을 처리한다, 기본값 / b : 이진모드, 이진 파일을 처리
'''
## 파일을 이용한 입력
'''
파일 입력 관련 : read(), readline(), readlines()
파일 출력 관련 : write(), writelines()
'''
## 한 행씩 읽어 들이기
'''
readline() 함수 사용
파일로 데이터 입력 후 이를 화면에 출력하는 프로그램
* 확장명 확인 필요.
'''
## with ~ as 문
'''
프로그램을 만들다 보면 close() 함수를 호출하지 않고 프로그램을 종료해서 종종
문제가 발생함. 아에 close() 함수를 하용하지 않으려면, with ~ as 문으로 파일을
열면 파일명.close()를 사용하지 않는다.
'''
## 도스 명령어 type의 구현
'''
지정한 파일의 내용을 화면에 출력 : type 파일명
'''
## 파일을 이용한 출력
'''
출력 결과를 파일에 저장하는 방식(파일에 내용 쓸 때 write()나 writelines() 함수 사용)
'''
## 도스 copy 명령어의 구현
'''
copy 소스파일 타깃파일
'''
## comp(소스파일, 타깃파일) : 소스파일과 타깃파일이 같은지 비교
## 암호화
'''
ord() 와 chr() 함수 사용
ord("파") # 출력 54028
chr(54028) # 출력 파
파를 암호화 하려고 54028("파")+100=54128("")으로 저장
num = ord("팸")
chr(num-100) # 출력 파
'''
## 파일 처리에서 조금 더 고려할 사항
'''
1. readline()과 readlines()
 readline() 함수는 한번에 한 행씩 읽어 들여 모든 행을 처리하려면
 반복문을 통해 계속 읽어 들여야 함
 readlines() 함수는 파일로 한번에 읽어 리스트에 저장
 파일 용량이 크면 리스트의 크기만큼 메모리를 사용해야 하기 때문에 문제 발생
 소지가 있음
 용량에 따라 두가지를 나눠서 사용해야 바람직함
2. 간단한 파일처리
 파일 입출력을 위해 with ~ as 문을 선호 하는 경우도 있음
 with ~ as 문을 사용하면 텍스트 파일을 복사하는것도 간단하게 표현 가능
'''
## 파일 및 디렉터리 다루기
'''
shutil 모듈과 os 모듈, os.path 모듈 : 파일, 디렉터리(폴더) 다룰 수 있는 다양한 함수 제공
import shutil # 파일 복사, 이동, 삭제
print(dir(shutil))
import os
print(dir(os))
print(os.getcwd()) # 현재 폴더 위치확인
import os.path # 경로 확인
print(dir(os.path))
'''
## 파일 및 디렉터리 복사
'''
import shutil
shutil.copy("test.txt","test3.txt") # 파일 복사
shutil.copy("D:\java_class\python_class\img","D:\java_class\python_class\img2") # 폴더 복사
'''
## 디렉터리의 생성 및 삭제
## 디렉터리의 생성 : os.mkdir("폴더명") 함수 사용
## 디렉터리의 삭제 : shutil.retree("폴더명") 함수 사용
'''
import os
import shutil
os.mkdir("d:/python_class/")
os.mkdir("d:/python_class/code")
shutil.rmtree("d:/python_class/")

'''
## 디렉터리의 목록 모두 보기 : os.walk(폴더) 함수 사용
'''
import os
for dirName, subDirList, fnames in os.walk("D:\\java_class\\python_class"):
    for fname in fnames:
        file_path = os.path.join(dirName, fname)
        print(file_path)
'''
'''
for문 : os.walk(폴더) 함수는 현재 폴더명(dirName), 
        현재 폴더의 하위 디렉터리 목록(subDirList),
        파일명 목록(fnames) 3개를 반환
for문2 : fname의 개수만큼 반복해서 폴더명과 파일명 묶어 출력
'''
## 파일 또는 디렉터리가 이미 존재하는지 확인
'''
import os.path
print(os.path.exists("c:/Windows/notepad.exe")) # True
print(os.path.isfile("c:/Windows/notepad.exe")) # True
print(os.path.isdir("c:/Windows")) # True
'''
## 파일 삭제
'''
import os
os.remove("삭제할 파일경로와 파일명")
있으면 삭제 되고
없으면 FileNotFoundError : [WinError 2] 지정된 파일을 찾을 수 없습니다 : "삭제할파일경로와파일명"
'''
## 파일 크기 확인(바이트 단위로 출력)
'''
import os.path
print(os.path.getsize("D:\java_class\python_class\img\GIF\cat.gif"))
'''
## 파일 압축 : zipfile모듈에서 제공
'''
import zipfile
newZip = zipfile.ZipFile("c:/Temp/new.zip", "w")
newZip.write("c:/Windows/notepad.exe", compress_type = zipfile.ZIP_DEFLATED)
newZip.close()
'''
'''
압축될 파일을 쓰기로 준비
압축 수행
압축 파일 닫기
'''
## 파일 압축 풀기 : zipfile모듈에서 제공
'''
import zipfile
extZip = zipfile.ZipFile("c:/Temp/new.zip", "r")
extZip.extractall("c:/Temp/")
extZip.close()
'''
'''
압축 풀 파일을 읽기로 준비
해당 폴더에 압축 풀기
압축 파일 닫기
'''
## 예외 처리 : try, except 문
## 에외 처리(Exception Handling) : 오류가 발생할 때 파이썬이 처리하지 않고 프로그래머가 작성 한 코드를 실행하는 방식
'''
import os
try:
    os.remove("c:/Temp/noFile.exe")
except:
    print("그런 파일 없어")
try, except 문 활용, 오류 대신 직접 오류 내용 작성 정상적으로 흐름을 이어감
'''
## except 문 뒤에 아무것도 명시 하지 않으면 모든 종류의 오류 처리
## 필요하다면 오류의 종류에 따라 다른 오류 처리도 가능
'''
try:
    실행할 문장들
except 예외_종류1:
    오류일 때 실행할 문장들
except 예외_종류2:
    오류일 때 실행할 문장들
'''
## 대표적인 예외 종류
'''
ImportError : import 문에서 오류가 발생할 때
IndexError : 리스트 등 첨자의 범위를 벗어날 때
KeyError : 딕셔너리에서 키가 없을 때
KeyboardInterrupt : 프로그램 실행 중 Ctrl+c를 누를 때
NameError : 변수명이 없는 것에 접근할 때
RecursionError : 재귀 호출의 횟수가 시스템에서 설정한 것 보다 넘칠때 (1000번)
RuntimeError : 실행이 발생할 때
SyntaxError : exec()나 eval()에서 문법상 오류가 발생할 때
TypeError : 변수형의 오류가 발생할 때 ex)문자열-문자열 연산
ValueError : 함수의 매개변수에 잘못된 값을 넘길 때 ex) int("파이썬")
ZeroDivisionError : 0으로 나눌 때
IOError : 파일 처리 등 오류일 때
'''