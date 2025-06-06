'''
기차 여러 대의 수송량을 합산하여 순위를 매겨보자
'''
import operator

trainTupleList = [('토마스',5),('헨리',8),('에드웟',9),('에밀리',5),
                  ('토마스',4),('헨리',7),('토마스',3),('에밀리',8),
                  ('머시',5),('고든',13)]

trainDic, trainList = {}, []
tmpTup = None
totalRank, currentRank = 1, 1

if __name__ == "__main__":
    for tmpTup in trainTupleList:
        tName = tmpTup[0]
        tWeight = tmpTup[1]
        if tName in trainDic:
            trainDic[tName] += tWeight
        else:
            trainDic[tName] = tWeight
    print("기차 수송량 목록 : ", trainTupleList)
    print("----------------------------------")
    trainList=sorted(trainDic.items(), key = operator.itemgetter(1),reverse=True)

    print("기차 \t 총수송량 \t 순위")
    print("----------------------------------")
    print(trainList[0][0],'\t',trainList[0][1],'\t',currentRank)
    for i in range(1, len(trainList)):
        totalRank += 1
        if trainList[i][1] == trainList[i-1][1]: ##앞 기차와 수송량이 같으면
            pass
        else:
            currentRank = totalRank
        print(trainList[i][0],'\t',trainList[i][1],'\t',currentRank)
