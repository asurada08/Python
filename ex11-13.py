myStr = "파이썬은 재미 있어요. 파이썬만 매일 공부하고 싶어요. ^^"
strPosList = []
index = 0

while True:
    index = myStr.index("파이썬", index)
    strPosList.append(index)
    index += 1
    
print("파이썬 글자 위치 : ", strPosList)
## ValueError: substring not found 오류 발생
## 해당 글자가 위치한 첨자 찾은 후 더이상 없기 때문에 오류가 발생