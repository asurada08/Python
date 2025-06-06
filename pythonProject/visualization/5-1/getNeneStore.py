import re

from ChickenUtil import ChickenStore

##############################################
brandName = 'nene'
base_url = 'https://nenechicken.com/17_new/sub_shop01.asp'


##############################################
def getData():
    savedData = []
    for page_idx in range(1, 47 + 1):
        url = base_url + '?page=%d' % (page_idx)
        chknStore = ChickenStore(brandName, url)
        soup = chknStore.getSoup()

        tablelists = soup.findAll('table', attrs={'class': 'shopTable'})
        # print(len(tablelists))
        for onetable in tablelists:
            store = onetable.select_one('.shopName').string
            # print(store)

            temp = onetable.select_one('.shopAdd').string
            #             print(temp)

            # 주소 접미사
            im_address = onetable.select_one('.shopMap')
            im_address = im_address.a['href']
            #             print(im_address)
            regex = '\d\S*'
            pattern = re.compile(regex)
            mymatch = pattern.search(im_address)
            addr_suffix = mymatch.group().replace("');", '')
            #             print(addr_suffix) # 주소 접미사

            print(type(addr_suffix))
            print(temp)
            print(addr_suffix)
            try:
                address = temp + ' ' + addr_suffix
                print(address)
            except:
                print("매장 주소 없음")
                address = "주소 이상"
                temp = "주소 이상"

            imsi = temp.split(' ')
            print(imsi)
            sido = imsi[0]
            gungu = imsi[1]

            phone = onetable.select_one('.tooltiptext').string
            # print(phone)

            mydata = [brandName, store, sido, gungu, address, phone]
            savedData.append(mydata)

            # end for statement

    chknStore.save2Csv(savedData)


##############################################
print(brandName + ' 매장 크롤링 시작')
getData()
print(brandName + ' 매장 크롤링 끝')