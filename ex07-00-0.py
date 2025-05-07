## 리스트
aa = []
for i in range(0, 100):
    aa.append(0)
b=len(aa)
print(b)

## 음수 값으로 접근(역순?)
bb = [10, 20, 30, 40]
print("bb[-1]은 %d, bb[-2]는 %d" % (bb[-1], bb[-2]))

## 리스트에 접근할 때 콜론:을 사용해 범위를 지정
cc = [10, 20, 30, 40]
print(cc[0:3])
print(cc[2:4])
##콜론의 앞이나 뒤 숫자 생략
print(cc[2:]) ##2부터 끝까지
print(cc[:2]) ##처음부터 2까지

## 리스트끼리 덧셈(리스트 결합?), 곱셈(리스트 복제?) 연산 
dd = [10, 20, 30]
ee = [40, 50, 60]
print(dd+ee)
print(dd*3)

## 리스트의 항목 건너뛰며 추출(음수는 역순?)
ff = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(ff[::2]) ##1칸 건너뛰고 출력
print(ff[::-2]) ##1칸 건너뛰고 역순 출력
print(ff[::-1]) ##역순으로 출력

## 값을 1개 변경
gg = [1, 2, 3]
gg[0] = 10
print(gg)

## 두번째 값 인 2를 200, 201이라는 값 2개로 변경
hh = [1, 2, 3]
hh[1:2] = [200, 201]
print(hh)

##list 안에 list 삽입
ii = [1, 2, 3]
ii[1] = [200, 201]
print(ii)

## 해당 항목 삭제
jj =  [1, 2, 3]
del(jj[1])
print(jj)

## kk[1]에서 kk[3]까지 삭제
kk = [1, 2, 3, 4, 5]
kk[1:4] = []
print(kk)

## list 자체를 삭제 하는 방법
ll =  [1, 2, 3]; ll=[]; print(ll)
ll =  [1, 2, 3]; ll=None; print(ll)
##ll =  [1, 2, 3]; del(ll); print(ll) ll list 자체를 삭제하여 출력 못함
