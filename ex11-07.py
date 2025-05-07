outFp = None
outStr = ""

outFp = open("test.txt", "w")

while True:
    outStr = input("내용 입력 : ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close()
print("정상적으로 파일에 씀")
'''
4행 : 파일을 열 때 쓰기 모드인 w 사용
6~11행 : 무한반복
7행 : 파일에 쓸 내용을 입력
8행 : 입력한 글자가 비어 있지 않으면 9행에서 입력한 내용을 파일에 씀
      입력한 글자가 비어 있다면 10 ~ 11행에서 무한 반복 종료
9행 : outStr만 파일에 쓴다면 여러 줄을 써도 줄 바꿈 되지 않고 한줄에
      이어서 써짐. 이를 방지하려고 행을 넘기는 \n을 사용
13행 : 파일 닫기
14행 : 메시지 출력
'''