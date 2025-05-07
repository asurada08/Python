from pandas import DataFrame

sdata={'사원':['서울','윤봉길','윤봉길','유관순','유관순'],
       '분기':[1,2,3,1,2],
       '실적':[800,200,500,400,700]
       }
myindex=['하나','둘','셋','넷','다섯']
myframe=DataFrame(sdata,index=myindex)

print(myframe)
