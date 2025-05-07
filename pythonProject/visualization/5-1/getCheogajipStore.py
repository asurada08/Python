from itertools import count
from ChickenUtil import ChickenStore
############################################
brandName = 'cheogajip' 
base_url = 'http://www.cheogajip.co.kr/bbs/board.php'
############################################
def getData():
    savedData = []  # 엑셀로 저장할 리스트
    
    for page_idx in count() :
        url = base_url 
        url += '?bo_table=store'
        url += '&page=%s' % str(page_idx+1)

        chknStore = ChickenStore(brandName, url)
        soup = chknStore.getSoup() 
        
        mytbody = soup.find('tbody')
        
        shopExists = False  # 매장 목록이 없다고 가정
        
        for mytr in mytbody.findAll('tr'):
            shopExists = True
#             print(page_idx+1)
#             print(mytr)
#             print('b' * 30)            

            try :
                store = mytr.select_one('td:nth-of-type(1)').string
                address = mytr.select_one('td:nth-of-type(2)').string
                phone = mytr.select_one('td:nth-of-type(3)').string
                print(store)
                print(address)
                print(phone)
                imsi = address.split(' ')
                print(imsi)

                sido = imsi[0]
                gungu = imsi[1]
                print(store + '  ' + phone)
                # exit()
                savedData.append([brandName, store, sido, gungu, address, phone])
                
            except AttributeError as err :
                print(err)
                shopExists = False
                break
            
#         if page_idx == 0 :
        if shopExists == False :
            chknStore.save2Csv(savedData)
            break
############################################
print(brandName + ' 매장 크롤링 시작')
getData()
print(brandName + ' 매장 크롤링 끝')