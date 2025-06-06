import sqlite3

## 전역 변수 선언 부분 ##
inStr = "'죽는 날까지 하늘을 우러러 한 점 부끄럼이 없기를, 잎새에 이는 바람에도 나는 괴로워했다. 별을 노래하는 마음으로 모든 죽어가는 것을 사랑해야지. 그리고 나한테 주어진 길을 걸어가야겠다. 오늘 밤에도 별이 바람에 스치운다'"
con, cur = None, None
onechar, count = "", 0

## 메인 코드 부분 ##
if __name__ == "__main__":
    con = sqlite3.connect("naverDB")
    cur = con.cursor()
    cur.execute("drop table if exists countTable")
    cur.execute("create table countTable(onechar text, count int)") # 문자, 개수
    
    for ch in inStr:
        if 'ㄱ' <= ch <= '힣':
            cur.execute("select * from countTable where onechar = '" + ch +"'")
            row = cur.fetchone() # 실행된 쿼리의 결과로 부터 첫번째 행을 가져옴
            if row == None:
                cur.execute("insert into countTable values('"+ ch + "'," + str(1) +")")
            else:
                cnt = row[1]
                cur.execute("update countTable set count =" + str(cnt+1) + " where onechar = '" + ch + "'")
    
    con.commit()
    
    cur.execute("select * from countTable order by count desc")
    print("원문\n", inStr)
    print("--------------------------------")
    print("문자\t빈도수")
    print("--------------------------------")
    
    while (True):
        row = cur.fetchone()
        if row == None:
            break;
        ch = row[0]
        cnt = row[1]
        print("%4s  %5d" % (ch, cnt))
    
    con.close()