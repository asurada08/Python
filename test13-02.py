import sqlite3

## 변수 선언 부분 ##
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql, sql2 = "", ""

## 메인 코드 부분 ##
con = sqlite3.connect("naverDB")
cur = con.cursor()
#sql = "create table productTable (pCode char(5), pName char(15), price int, amount int)"
#cur.execute(sql)

while (True):
    data1 = input("pCode : ")
    if data1 == "":
        break;
    data2 = input("pName : ")
    data3 = input("price : ")
    data4 = input("amount : ")
    
    sql2 = "insert into productTable values('"+ data1 + "','" + data2  + "','" + data3  + "','" + data4 +"')"
    cur.execute(sql2)
    
con.commit()
con.close()