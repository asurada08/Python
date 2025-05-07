from pandas import Series

mylist = [10, 40, 30]
myindex = ['김유신', '이순신', '강감찬']

print("\n#케이스 01")
myseries = Series(mylist)
print(myseries)

print("\n#케이스 02")
myseries = Series(data=mylist)
print(myseries)

print("\n#케이스 03")
myseries = Series(data=mylist, index=myindex)
print(myseries)

print("\n#케이스 04")
myseries = Series(data=mylist, index=myindex, dtype=float)
print(myseries)

# Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
