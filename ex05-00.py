a = 99
if a < 100:
    print("100보다 작군요.")

jumsu = 55
res = ""
'''
if jumsu >= 60:
    res = "합격"
else:
    res = "불합격"
print(res)
'''
res="합격" if jumsu >= 60 else "불합격"
print(res)


fruit = ["사과", "배", "딸기", "포도"]
fruit.append("귤")
print(fruit,"\n",fruit[1],fruit[4],"\n",type(fruit),id(fruit))
if "딸기" in fruit:
    print("딸기 있네요~")
