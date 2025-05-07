myList = [30, 10, 20]
print("현재 리스트 : %s" % myList)

myList.append(40)
print("append(40) 이후 : %s" % myList)

print("pop()으로 추출한 값 : %s" % myList.pop())
print("pop() 이후 : %s" % myList)

myList.sort()
print("sort() 이후 : %s" % myList)

myList.reverse()
print("reverse() 이후 : %s" % myList)

print("20값의 위치 : %d" % myList.index(20))

myList.insert(2, 222)
print("insert(2, 222) 이후 : %s" % myList)

myList.remove(222)
print("remove(222) 이후 : %s" % myList)

myList.extend([77, 88, 77])
print("extend([77, 88, 77]) 이후 : %s" % myList)

print("77값의 개수 : %d" % myList.count(77))

aList = [30, 10, 20]
newList = sorted(aList)
print("aList : %s" % aList)
print("sorted() 후 aList : %s" % aList)
print("sorted() 후 newList : %s" % newList)
