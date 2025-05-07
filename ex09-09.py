## 함수 선언 부분 ##
def multi(v1, v2):
    retList = [] # 빈 리스트 준비
    res1 = v1 + v2
    res2 = v1 - v2
    retList.append(res1) # 리스트에 값 추가
    retList.append(res2) # 리스트에 값 추가
    return retList # 리스트 반환

## 전역 변수 선언 부분 ##
myList = []
hap, sub = 0, 0

## 메인 코드 부분 ##
myList =  multi(100, 200)
hap = myList[0]
sub = myList[1] # 15 ~ 17 반환한 리스트의 값을 각 변수에 대입
print("multi()에서 돌려준 값 : %d, %d" % (hap, sub))
