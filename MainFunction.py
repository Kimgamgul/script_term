# -*- coding: utf-8 -*-
loopFlag = 1

from SeperatedFuction import *

#==============================================================================

#Main
def printMenu1():
    print("All In Trip Menu!")
    print("1.국내")
    print("2.국외")
    print("------------------------------------")
    funcComm = int(input())
    if funcComm == 1:
        printMenuLocal()
    elif funcComm == 2:
        selectContinent()
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
        selectLocalMenu()
    elif localNum == 1:#경기
        selectLocalMenu() 
    elif localNum == 2:#인천
        selectLocalMenu() 
    elif localNum == 3:#강원도
        selectLocalMenu()     
    elif localNum == 4:#충청도
        selectLocalMenu()   
    elif localNum == 5:#전라도
        selectLocalMenu()   
    elif localNum == 6:#경상도
        selectLocalMenu()
#==============================================================================
        
#국내3-1
def selectLocalMenu():
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
        selectFunction(MenuNum-1)
    else:
        selectLocalMenu()
#==============================================================================
        
#국내3-2
def selectFunction(MenuComm):
    if MenuComm == 0:
        printHotel()
    elif MenuComm == 1:
        printRestaurant()
    elif MenuComm == 2:
        printFestival()
    elif MenuComm == 3:
        printTourPlace()
    elif MenuComm == 4:
        printHospital()
    elif MenuComm == 5:
        printToilet()
    elif MenuComm == 6:
        printWifi()
#==============================================================================
        
def printHotel():
    #여기서 호텔 정보 출력
    print("숙박 정보입니다.")
    #데이터 수신 및 출력

def printRestaurant():
    print("음식점 정보입니다.")
    
    
def printFestival():
    print("행사 정보입니다.")
    
    
def printTourPlace():
    print("관광지 정보입니다.")

    
def printHospital():
    print("병원 정보입니다.")

def printToilet():
    print("화장실 정보입니다.")

def printWifi():
    print("와이파이 정보입니다.")
    
#============================================================================== 
#==============================================================================    
    
#국외1-1  
def selectContinent():
    print("All In Trip")
    print("원하는 대륙을 선택해 주세요")
    print("1.아시아")
    print("2.유럽")
    print("3.북아메리카")
    print("4.남아메리카")
    print("5.아프리카")
    print("6.오세아니아")
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
        selectNorthAmerica()
    elif ContNum == 3:
        selectSouthAmerica()
    elif ContNum== 4:
        selectAfrica()
    elif ContNum == 5:
        selectOceania()
#============================================================================== 
#국외2       
 
def selectAsia():
    print("아시아 국가 선택")
    selectWorldMenu()

def selectEurope():
    print("유럽 국가선택")
    selectWorldMenu()

def selectNorthAmerica():
    print("북아메리카 국가선택")
    selectWorldMenu()

def selectSouthAmerica():
    print("남아메리카 국가선택")
    selectWorldMenu()

def selectAfrica():
    print("아프리카 국가선택")
    selectWorldMenu()

def selectOceania():
    print("오세아니아 국가선택")  
    selectWorldMenu()
    
#==============================================================================            
#국외3-1
def selectWorldMenu():
    print("All In Trip")
    print("원하는 기능을 선택해 주세요")    
    print("1.기본정보")
    print("2.여행경보")
    print("3.안전정보")
    print("4.옷차림정보")
    print("-------------------------------------------")
    MenuComm = int(input()) #메뉴 번호 입력
    if 0< MenuComm and MenuComm<5:
        selectWorldFunction(MenuComm-1)
    else:
        selectWorldMenu()          
#==============================================================================
        
#국외3-2
def selectWorldFunction(MenuComm):
    if MenuComm == 0:
        printWorldBasicInfo()
    elif MenuComm == 1:
        printWorldWarning()
    elif MenuComm == 2:
        printWorldSafty()
    elif MenuComm == 3:
        printClothes()
        
#==============================================================================
        
def printWorldBasicInfo():
    print("세계 기본 정보입니다.")

 
def printWorldWarning():
    print("세계 여행 경보 입니다.")


def printWorldSafty():
    print("세계 현지 안전 정보입니다.")
    
    
def printClothes():
    month = int(input("해당 국가의 옷차림 정보를 알고 싶은 월을 입력하세요:"))
    
        
        



        







      