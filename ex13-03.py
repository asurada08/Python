import sqlite3
from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def insertData():
    con, cur = None, None
    data1, data2, data3, data4 = "", "", "", ""
    sql = ""
    
    con = sqlite3.connect("naverDB")
    cur = con.cursor()
    
    data1 = edt1.get(); data2 = edt2.get(); data3 = edt3.get(); data4 = edt4.get()
    try:
        sql = "insert into userTable values('" + data1 + "','" + data2 + "','" + data3 + "','" + data4 + "')"
        cur.execute(sql)        
    except:
        messagebox.showerror("오류", "데이터 입력 오류가 발생함")
    else:
        messagebox.showinfo("성공", "데이터 입력 성공")
    con.commit()
    con.close()
    
def selectData():
    strData1, strData2, strData3, strData4 = [], [], [], []
    con = sqlite3.connect("naverDB")
    cur = con.cursor()
    cur.execute("select * from userTable")
    strData1.append("사용자ID"); strData2.append("사용자이름") 
    strData3.append("이메일"); strData4.append("출생연도")
    strData1.append("------------"); strData2.append("------------")
    strData3.append("------------"); strData4.append("------------")
    while (True):
        row = cur.fetchone()
        if row == None:
            break;
        strData1.append(row[0]); strData2.append(row[1])
        strData3.append(row[2]); strData4.append(row[3])
        
    listData1.delete(0, listData1.size() - 1); listData2.delete(0, listData2.size() - 1)
    listData3.delete(0, listData3.size() - 1); listData4.delete(0, listData4.size() - 1)
    for item1, item2, item3, item4 in zip(strData1, strData2, strData3, strData4):
        listData1.insert(END, item1); listData2.insert(END, item2)
        listData3.insert(END, item3); listData4.insert(END, item4)
    con.close()
    
## 메인 코드 부분 ##
window = Tk()
window.geometry("600x300")
window.title("GUI 데이터 입력")

edtFrame = Frame(window)
edtFrame.pack()
listFrame = Frame(window)
listFrame.pack()

edt1 = Entry(edtFrame, width = 10); edt1.pack(side = LEFT, padx = 10, pady = 10)
edt2 = Entry(edtFrame, width = 10); edt2.pack(side = LEFT, padx = 10, pady = 10)
edt3 = Entry(edtFrame, width = 10); edt3.pack(side = LEFT, padx = 10, pady = 10)
edt4 = Entry(edtFrame, width = 10); edt4.pack(side = LEFT, padx = 10, pady = 10)

btnInsert = Button(edtFrame, text = "입력", command = insertData)
btnInsert.pack(side = "left", padx = 10, pady = 10)
btnSelect = Button(edtFrame, text = "조회", command = selectData)
btnSelect.pack(side = "left", padx = 10, pady = 10)

listData1 = Listbox(listFrame, bg = "yellow")
listData1.pack(side = LEFT, fill = BOTH, expand = 1)
listData2 = Listbox(listFrame, bg = "yellow")
listData2.pack(side = LEFT, fill = BOTH, expand = 1)
listData3 = Listbox(listFrame, bg = "yellow")
listData3.pack(side = LEFT, fill = BOTH, expand = 1)
listData4 = Listbox(listFrame, bg = "yellow")
listData4.pack(side = LEFT, fill = BOTH, expand = 1)

window.mainloop()
'''
6~23행 : <입력> 버튼을 누를 때 실행되는 함수로 데이터 입력
14행 : 화면에 있는 텍스트박스 4개에서 값을 가져옴
15~21행 : SQL문으 만들어 실행하는데, 17행에서 오류가 발행해도 프로그램
          종료되지 않게 try문 활용
25~46행 : <조회> 버튼을 누를 때 실행되는 함수로 데이터 입력
26행 : strData1은 사용자ID 열의 결과를 리스트박스에 출력하는 리스트
30행, 32행 : 제목을 리스트에 추가
38행 : 모든 사용자ID 추가
41~42행 : 화면에 있는 리스트 박스 4개를 모두 비움
43~45행 : 각 리스트박스에 앞에서 준비한 strData1~4의 값을 다시 채움
53~56행 : 화면 분할 위해 프레임 2개 준비

'''