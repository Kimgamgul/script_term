# -*- coding: utf-8 -*-
#==============================================================================    

from SeperatedFunction import * 
from excel import * 

loopFlag = 1   
#국외1-1  
save = None
def init():
    f = Functions("apis.data.go.kr","/1262000/CountryBasicService/getCountryBasicList","j%2Bbq5FUNW828jPaqGs8emef8UinsgGbIyBjQT4ZaXSyhgAj8%2B2QqnTzHYZiG52%2BprkbQfeOY0JSWYvB01wqQ8Q%3D%3D&numOfRows=999",)
    f.userURIBuilder()
    f.loadFromWeb()
    f.saveOverseas()    
    
def selectContinent():
    init()
    print("All In Trip")
    print("원하는 대륙을 선택해 주세요")
    print("1.아시아/태평양")
    print("2.유럽")
    print("3.미주")
    print("4.중동/아프리카")
    ContNum = int(input())
    if 0<ContNum and ContNum<7:
        printWorld(ContNum-1)
    else:
        selectContinent()
#==============================================================================
#국외1-2
def printWorld(ContNum):
    if ContNum == 0:
        selectAsia()
    elif ContNum == 1:
        selectEurope()
    elif ContNum == 2:
        selectAmerica()
    elif ContNum == 3:
         selectAfrica()

#============================================================================== 
def selectAsia():
    print("아시아/태평양 국가 선택")
    for k,v in overseasAsiad.items():
            print(k,". ",v)
            
    num = int(input("번호: "))        
    save = overseasAsiad[num]        
    selectWorldMenu(save)
    
def selectEurope():
    print("유럽 국가선택")
    for k,v in overseasEUd.items():
            print(k,". ",v)
            
    num = int(input("번호: "))        
    save = overseasEUd[num]        
    selectWorldMenu(save)

def selectAmerica():
    print("미주 국가선택")
    for k,v in overseasAmericad.items():
            print(k,". ",v)
            
    num = int(input("번호: "))        
    save = overseasAmericad[num]        
    selectWorldMenu(save)

def selectAfrica():
    print("중동/아프리카 국가선택")
    for k,v in overseasAfricad.items():
            print(k,". ",v)
            
    num = int(input("번호: "))        
    save = overseasAfricad[num]        
    selectWorldMenu(save)
    
def selectWorldMenu(save):
    print("All In Trip")
    print("원하는 기능을 선택해 주세요")    
    print("1.기본정보")
    print("2.여행경보")
    print("3.안전정보")
    print("4.옷차림정보")
    print("-------------------------------------------")
    MenuComm = int(input()) #메뉴 번호 입력
    if 0< MenuComm and MenuComm<5:
        selectWorldFunction(MenuComm-1,save)
    else:
        selectWorldMenu()      

#국외3-2
def selectWorldFunction(MenuComm,save):
    if MenuComm == 0:
        printWorldBasicInfo(save)
    elif MenuComm == 1:
        printWorldWarning(save)
    elif MenuComm == 2:
        printWorldSafty(save)
    elif MenuComm == 3:
        printClothes(save)
        
#==============================================================================
        
def printWorldBasicInfo(save):
    print("세계 기본 정보입니다.")
    f = Functions("apis.data.go.kr","/1262000/CountryBasicService/getCountryBasicList","j%2Bbq5FUNW828jPaqGs8emef8UinsgGbIyBjQT4ZaXSyhgAj8%2B2QqnTzHYZiG52%2BprkbQfeOY0JSWYvB01wqQ8Q%3D%3D&numOfRows=999",)
    f.userURIBuilder()
    f.loadFromWeb()
    f.extractcountryData("item",save,"basic")

 
#def printWorldWarning(save):
#    print("세계 여행 경보 입니다.")
#    f = Functions("apis.data.go.kr","/1262000/TravelWarningService/getTravelWarningList","j%2Bbq5FUNW828jPaqGs8emef8UinsgGbIyBjQT4ZaXSyhgAj8%2B2QqnTzHYZiG52%2BprkbQfeOY0JSWYvB01wqQ8Q%3D%3D&numOfRows=999",)
#    f.userURIBuilder()
#    f.loadFromWeb()
#    f.extractFilterData("item","wrtDt")


def printWorldSafty(save):
    print("세계 현지 안전 정보입니다.")
    f = Functions("apis.data.go.kr","/1262000/CountrySafetyService/getCountrySafetyList","j%2Bbq5FUNW828jPaqGs8emef8UinsgGbIyBjQT4ZaXSyhgAj8%2B2QqnTzHYZiG52%2BprkbQfeOY0JSWYvB01wqQ8Q%3D%3D&numOfRows=999",)
    f.userURIBuilder()
    f.loadFromWeb()
    f.saveContent(save)
    
def printClothes(save):
    e = ExcelImport("clothes.xlsx")
    e.loadFile()
    e.filterPrint(0,save)    


#==============================================================================
#============================================================================== 
#==============================================================================

#Main
def printMenu1():
    init()
    print("All In Trip Menu!")
    print("1.국내")
    print("2.국외")
    print("3.종료")
    print("------------------------------------")
    funcComm = int(input())
    if funcComm == 1:
        printMenuLocal()
    elif funcComm == 2:
        selectContinent()
    elif funcComm == 3:
         QuitBookMgr()
#==============================================================================
        
#국내1
def printMenuLocal():
    print("All In Trip 국내 메뉴입니다.")
    print("1.서울")
    print("2.경기")
    print("3.인천")
    print("4.강원도")
    print("5.충청도")
    print("6.전라도")
    print("7.경상도")
    localNum = int(input())
    #위에 정보 저장하고 메뉴로 넘어가야할듯한
    if 0<localNum and localNum <8:
        printMenuLocalDetail(localNum-1)
    else:
        printMenuLocal()
        
#==============================================================================        
#국내2        
def printMenuLocalDetail(localNum): #세부적인 코드 추가해야함
    
    if localNum == 0:#서울
        selectLocalMenu(localNum)
    elif localNum == 1:#경기
        selectLocalMenu(localNum) 
    elif localNum == 2:#인천
        selectLocalMenu(localNum) 
    elif localNum == 3:#강원도
        selectLocalMenu(localNum)     
    elif localNum == 4:#충청도
        selectLocalMenu(localNum)   
    elif localNum == 5:#전라도
        selectLocalMenu(localNum)   
    elif localNum == 6:#경상도
        selectLocalMenu(localNum)
#==============================================================================
        
#국내3-1
def selectLocalMenu(localNum):
    print("All In Trip")
    print("원하는 기능을 선택해 주세요")    
    print("1.숙박")
    print("2.음식점")
    print("3.행사")
    print("4.관광지")
    print("5.병원")
    print("6.화장실")
    print("7.와이파이")
    print("-------------------------------------------")
    MenuNum = int(input()) #메뉴 번호 입력
    if 0< MenuNum and MenuNum<8:
        selectFunction(MenuNum-1,localNum)
    else:
        selectLocalMenu()
#==============================================================================
        
#국내3-2
def selectFunction(MenuComm,localNum):
    if MenuComm == 0:
        printHotel(localNum)
    elif MenuComm == 1:
        printRestaurant(localNum)
    elif MenuComm == 2:
        printFestival(localNum)
    elif MenuComm == 3:
        printTourPlace(localNum)
    elif MenuComm == 4:
        printHospital(localNum)
    elif MenuComm == 5:
        printToilet(localNum)
    elif MenuComm == 6:
        printWifi(localNum)
#==============================================================================
        
def printHotel(localNum):
    #여기서 호텔 정보 출력
    print("숙박 정보입니다.")
    e = ExcelImport("trip_info.xlsx")
    e.loadFile()
    if localNum == 0:#서울
        e.filterPrint(2,"Seoul")
    elif localNum == 1:#경기
        e.filterPrint(2,"Gyeonggi-do")
    elif localNum == 2:#인천
        e.filterPrint(2,"Incheon")
    elif localNum == 3:#강원도
        e.filterPrint(2,"Gangwon-do")    
    elif localNum == 4:#충청도
        e.filterPrint(2,"Chungcheongbuk-do")
    elif localNum == 5:#전라도   
        e.filterPrint(2,"Jeollabuk-do")
        e.filterPrint(2,"Gwangju")
        e.filterPrint(2,"Jeollanam-do")
    elif localNum == 6:#경상도
        e.filterPrint(2,"Gyeongsangbuk-do")
        e.filterPrint(2,"Gyeongsangnam-do")
        e.filterPrint(2,"Busan")
        e.filterPrint(2,"Deagu")
               
    #데이터 수신 및 출력
def printSelectFood():
    print("음식 종류를 입력하세요")
    print("1.분식")
    print("2.패스트 푸드")
    print("3.한식")
    print("4.경양식")
    print("5.중식")
    print("6.일식")
    print("7.카페")

def printRestaurant(localNum):
    printSelectFood()
    food = int(input())
    print("음식점 정보입니다.")
    if food== 1:
        e = ExcelImport("food_con.xlsx")
        e.loadSome(10)
        e.printSome(10)
    elif food == 2:
        e = ExcelImport("food_fast.xlsx")
        e.loadSome(10)
        e.printSome(10)
    elif food == 3:
        e = ExcelImport("food_kor.xlsx")
        e.loadSome(10)
        e.printSome(10)
    elif food == 4:
        e = ExcelImport("food_am.xlsx")
        e.loadSome(10)
        e.printSome(10)
    elif food == 5:
        e = ExcelImport("food_chi.xlsx")
        e.loadSome(10)
        e.printSome(10)
    elif food == 6:
        e = ExcelImport("food_jp.xlsx")
        e.loadSome(10)
        e.printSome(10)
    elif food == 7:
        e = ExcelImport("food_cafe.xlsx")
        e.loadSome(10)
        e.printSome(10)

    
    
def printFestival(localNum):
    print("행사 정보입니다.")
    
    if localNum == 0:#서울
        e = ExcelImport("fest_seoul.xlsx")
        e.loadFile()
        e.printInfo()
    elif localNum == 1:#경기
        e = ExcelImport("fest_gyoengggi.xlsx")
        e.loadFile()
        e.printInfo()
    elif localNum == 2:#인천
        e = ExcelImport("fest_Incheon.xlsx")
        e.loadFile()
        e.printInfo()
    elif localNum == 3:#강원도
        e = ExcelImport("fest_gangwon.xlsx")
        e.loadFile()
        e.printInfo()
    elif localNum == 4:#충청도
       e = ExcelImport("fest_chungbuk.xlsx")
       e.loadFile()
       e.printInfo()
       e = ExcelImport("fest_chungnam.xlsx")
       e.loadFile()
       e.printInfo()
       e = ExcelImport("fest_daejeon.xlsx")
       e.loadFile()
       e.printInfo()
    elif localNum == 5:#전라도   
        e = ExcelImport("fest_junnam.xlsx")
        e.loadFile()
        e.printInfo()
        e = ExcelImport("fest_junbuk.xlsx")
        e.loadFile()
        e.printInfo()
        e = ExcelImport("fest_gwangju.xlsx")
        e.loadFile()
        e.printInfo()
    elif localNum == 6:#경상도
        e = ExcelImport("fest_chungbuk.xlsx")
        e.loadFile()
        e.printInfo()
        e = ExcelImport("fest_chungnam.xlsx")
        e.loadFile()
        e.printInfo()
        e = ExcelImport("fest_busan.xlsx")
        e.loadFile()
        e.printInfo()
        e = ExcelImport("fest_busan.xlsx")
        e.loadFile()
        e.printInfo()
        e = ExcelImport("fest_daegu.xlsx")
        e.loadFile()
        e.printInfo()
        e = ExcelImport("fest_ulsan.xlsx")
        e.loadFile()
        e.printInfo()
    
def printTourPlace(localNum):
    print("관광지 정보입니다.")
    e = ExcelImport("sights.xlsx")
    e.loadFile()
    if localNum == 0:#서울
        e.filterPrint(4,"서울")
    elif localNum == 1:#경기
        e.filterPrint(4,"경기도")
    elif localNum == 2:#인천
        e.filterPrint(4,"인천")
    elif localNum == 3:#강원도
        e.filterPrint(4,"강원도")    
    elif localNum == 4:#충청도
        e.filterPrint(4,"충청북도")
        e.filterPrint(4,"충청남도")
        e.filterPrint(4,"대전")
    elif localNum == 5:#전라도   
        e.filterPrint(4,"전라북도")
        e.filterPrint(4,"전라남도")
        e.filterPrint(4,"광주")
    elif localNum == 6:#경상도
        e.filterPrint(4,"경상북도")
        e.filterPrint(4,"경상남도")
        e.filterPrint(4,"부산")
        e.filterPrint(4,"대구")
        e.filterPrint(4,"울산")
    
def printHospital(localNum):
    print("병원 정보입니다.")
    if localNum == 0:#서울
        f = Functions("openapi.hira.or.kr","/openapi/service/pharmacyInfoService/getParmacyBasisList","j%2Bbq5FUNW828jPaqGs8emef8UinsgGbIyBjQT4ZaXSyhgAj8%2B2QqnTzHYZiG52%2BprkbQfeOY0JSWYvB01wqQ8Q%3D%3D",sidoCd = "110000")
        f.loadFromWeb()
        f.extractBookData("item","addr","clCdNm","sgguCdNm","sidoCdNm","telno","yadmNm")
    elif localNum == 1:#경기
        f = Functions("openapi.hira.or.kr","/openapi/service/pharmacyInfoService/getParmacyBasisList","j%2Bbq5FUNW828jPaqGs8emef8UinsgGbIyBjQT4ZaXSyhgAj8%2B2QqnTzHYZiG52%2BprkbQfeOY0JSWYvB01wqQ8Q%3D%3D",sidoCd="310000")
        f.loadFromWeb()
        f.extractBookData("item","addr","clCdNm","sgguCdNm","sidoCdNm","telno","yadmNm")

    elif localNum == 2:#인천
        f = Functions("openapi.hira.or.kr","/openapi/service/pharmacyInfoService/getParmacyBasisList","j%2Bbq5FUNW828jPaqGs8emef8UinsgGbIyBjQT4ZaXSyhgAj8%2B2QqnTzHYZiG52%2BprkbQfeOY0JSWYvB01wqQ8Q%3D%3D",sidoCd = "220000")
        f.loadFromWeb()
        f.extractBookData("item","addr","clCdNm","sgguCdNm","sidoCdNm","telno","yadmNm")

    elif localNum == 3:#강원도
        f = Functions("openapi.hira.or.kr","/openapi/service/pharmacyInfoService/getParmacyBasisList","j%2Bbq5FUNW828jPaqGs8emef8UinsgGbIyBjQT4ZaXSyhgAj8%2B2QqnTzHYZiG52%2BprkbQfeOY0JSWYvB01wqQ8Q%3D%3D",sidoCd = "320000")
        f.loadFromWeb()
        f.extractBookData("item","addr","clCdNm","sgguCdNm","sidoCdNm","telno","yadmNm")
    
    elif localNum == 4:#충청도
        f = Functions("openapi.hira.or.kr","/openapi/service/pharmacyInfoService/getParmacyBasisList","j%2Bbq5FUNW828jPaqGs8emef8UinsgGbIyBjQT4ZaXSyhgAj8%2B2QqnTzHYZiG52%2BprkbQfeOY0JSWYvB01wqQ8Q%3D%3D",sidoCd = "330000")
        f.loadFromWeb()
        f.extractBookData("item","addr","clCdNm","sgguCdNm","sidoCdNm","telno","yadmNm")
    
    elif localNum == 5:#전라도   
        f = Functions("openapi.hira.or.kr","/openapi/service/pharmacyInfoService/getParmacyBasisList","j%2Bbq5FUNW828jPaqGs8emef8UinsgGbIyBjQT4ZaXSyhgAj8%2B2QqnTzHYZiG52%2BprkbQfeOY0JSWYvB01wqQ8Q%3D%3D",sidoCd = "350000")
        f.loadFromWeb()
        f.extractBookData("item","addr","clCdNm","sgguCdNm","sidoCdNm","telno","yadmNm")
        f = Functions("openapi.hira.or.kr","/openapi/service/pharmacyInfoService/getParmacyBasisList","j%2Bbq5FUNW828jPaqGs8emef8UinsgGbIyBjQT4ZaXSyhgAj8%2B2QqnTzHYZiG52%2BprkbQfeOY0JSWYvB01wqQ8Q%3D%3D",sidoCd = "240000")    
        f.loadFromWeb()
        f.extractBookData("item","addr","clCdNm","sgguCdNm","sidoCdNm","telno","yadmNm")

    elif localNum == 6:#경상도
        f = Functions("openapi.hira.or.kr","/openapi/service/pharmacyInfoService/getParmacyBasisList","j%2Bbq5FUNW828jPaqGs8emef8UinsgGbIyBjQT4ZaXSyhgAj8%2B2QqnTzHYZiG52%2BprkbQfeOY0JSWYvB01wqQ8Q%3D%3D",sidoCd = "210000")
        f.loadFromWeb()
        f.extractBookData("item","addr","clCdNm","sgguCdNm","sidoCdNm","telno","yadmNm")

        f = Functions("openapi.hira.or.kr","/openapi/service/pharmacyInfoService/getParmacyBasisList","j%2Bbq5FUNW828jPaqGs8emef8UinsgGbIyBjQT4ZaXSyhgAj8%2B2QqnTzHYZiG52%2BprkbQfeOY0JSWYvB01wqQ8Q%3D%3D",sidoCd = "380000")
        f.loadFromWeb()
        f.extractBookData("item","addr","clCdNm","sgguCdNm","sidoCdNm","telno","yadmNm")

        f = Functions("openapi.hira.or.kr","/openapi/service/pharmacyInfoService/getParmacyBasisList","j%2Bbq5FUNW828jPaqGs8emef8UinsgGbIyBjQT4ZaXSyhgAj8%2B2QqnTzHYZiG52%2BprkbQfeOY0JSWYvB01wqQ8Q%3D%3D",sidoCd = "260000")
        f.loadFromWeb()
        f.extractBookData("item","addr","clCdNm","sgguCdNm","sidoCdNm","telno","yadmNm")

def printToilet(localNum):
    print("화장실 정보입니다.")
    e = ExcelImport("toilet2.xlsx")
    e.loadFile()
    if localNum == 0:#서울
        e.filterPrint2(2,"서울")
    elif localNum == 1:#경기
        e.filterPrint2(2,"경기")
    elif localNum == 2:#인천
        e.filterPrint2(2,"인천")
    elif localNum == 3:#강원도
        e.filterPrint2(2,"강원")    
    elif localNum == 4:#충청도
        e.filterPrint2(2,"충청")
        e.filterPrint2(2,"대전")
    elif localNum == 5:#전라도   
        e.filterPrint2(2,"전라")
        e.filterPrint2(2,"광주")
    elif localNum == 6:#경상도
        e.filterPrint2(2,"경상")
        e.filterPrint2(2,"부산")
        e.filterPrint2(2,"대구")
        e.filterPrint2(2,"울산")
    
def printWifi(localNum):
    print("와이파이 정보입니다.")
    e = ExcelImport("wifi.xlsx")
    e.loadFile()
    if localNum == 0:#서울
        e.filterPrint(1,"서울")
    elif localNum == 1:#경기
        e.filterPrint(1,"경기")
    elif localNum == 2:#인천
        e.filterPrint(1,"인천")
    elif localNum == 3:#강원도
        e.filterPrint(1,"강원")    
    elif localNum == 4:#충청도
        e.filterPrint(1,"충북")
        e.filterPrint(1,"충남")
        e.filterPrint(1,"대전")
    elif localNum == 5:#전라도   
        e.filterPrint(1,"전북")
        e.filterPrint(1,"전남")
        e.filterPrint(1,"광주")
    elif localNum == 6:#경상도
        e.filterPrint(1,"경북")
        e.filterPrint(1,"경남")
        e.filterPrint(1,"부산")
        e.filterPrint(1,"대구")
        e.filterPrint(1,"울산")
    
#============================================================================== 

#3번누르면 나가기    
def QuitBookMgr():
    global loopFlag
    loopFlag = 0
    
while(loopFlag > 0):
   printMenu1()
else:
    print ("Thank you! Good Bye")
    