## 변수 선언 부분 ##
foods = {"떡볶이":"순대","짜장면":"탕수육","라면":"김치","피자":"피클","삼겹살":"소주","치킨":"맥주","오뎅":"국물"};

## 메인 코드 부분 ##
while (True):
    myfood = input(str(list(foods.keys())) + "중 좋아하는 음식은?")
    if myfood in foods:
        print("<%s> 궁합 음식은 <%s> 입니다" % (myfood, foods.get(myfood)))
    elif myfood == "끝":
        break
    else:
        print("그런 음식 없어요. 확인해 보세요")
