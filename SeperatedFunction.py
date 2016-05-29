# -*- coding: utf-8 -*-
from xml.dom.minidom import parse
from xml.etree import ElementTree
from http.client import HTTPConnection

xmlFD = -1
BooksDoc = None

##--------------------------------------------
overseasAsia = []
overseasAsiad = dict()
overseasEU = []
overseasEUd = dict()
overseasAmerica = []
overseasAmericad = dict()
overseasAfrica = []
overseasAfricad = dict()
##--------------------------------------------

class Functions:
    #이 함수는 파일에서 불러오기용  
    def __init__(self,Name,subName,regKey,**items):
        #Name은 "apis.data.go.kr"
        #subName은 그 뒤에 오는
        #/1262000/CountrySafetyService/getCountrySafetyList 이런거
        #regkey는 등록키
        #items는 pageNo = 999, NumOfRaw = 999이런 식으로 넣으면 됨
        self.conn = None
        self.subName = subName
        #두개는 생성자 오버로딩으로 regkey가 있다면
        #reg키를 넣는다.
        self.fileName = Name
        self.regKey = regKey
        #openAPI에서 필요한 URL을 만들기 위해서 diction형태로 초기화할때 넣어준다.
        self.items = items
        
    def userURIBuilder(self):
        if(self.subName != 0):
            str = "http://"+self.fileName +self.subName+"?"+"ServiceKey="+self.regKey+"&"
        else:
            str = "http://"+self.fileName+"?"+"ServiceKey="+self.regKey+"&"            
        for key in self.items.keys():
            str += key + "=" + self.items[key] + "&"
        return str[0:len(str)-1]
    def loadFromFile(self):
        global xmlFD,BooksDoc
        try:
            xmlFD = open(self.fileName)
        except IOError:
            print("invalid file name or path")
        else:
            try:
                dom = parse(xmlFD)
            except Exception:
                print("loadingFail!!")
            else:
                print("XML Document loading complete")
                self.dom = dom
                return dom
            return None

    def loadFromWeb(self):
        if self.conn == None:
            self.conn = HTTPConnection(self.fileName)
        url = self.userURIBuilder()
        #print(url)
        
        self.conn.request("GET",url)
        self.req = self.conn.getresponse()
        print(self.req.status)
        if int(self.req.status) == 200:
           print("download Complete!")
        else:
           print("API Call Failed")
           return None
           
    def extractBookData(self,treename,*itemName):
        tree = ElementTree.fromstring(self.req.read())
        #print(self.req.read())        
        # Book 엘리먼트를 가져옵니다.
        itemElements = tree.getiterator(treename)  # return list type
        
        print(itemElements)
        for item in itemElements:
            ls = []
            for x in itemName:
                ls.append(item.find(x))
           #print (strTitle)
            for x in ls:
                if len(x.text) >0:
                    print(x.text,end = " ")
            print("")        
##------------------------------------------------------------------------------
    def extractcountryData(self,treename,country,*itemName):
        tree = ElementTree.fromstring(self.req.read())
        itemElements = tree.getiterator(treename)  # return list type
        
        print(itemElements)
        for item in itemElements:
            cont = item.find("countryName")
            if country == cont.text:
                ls = []
                for x in itemName:
                    ls.append(item.find(x))
           #print (strTitle)
                for x in ls:
                    if len(x.text) >0:
                        print(x.text,end = " ")
                print("")        
                
##------------------------------------------------------------------------------           
    def saveOverseas(self):
        tree = ElementTree.fromstring(self.req.read())
        itemElements = tree.getiterator("item")
        for item in itemElements:
            continent = item.find("continent")
            country = item.find("countryName")
            if continent.text == "아시아/태평양":
                overseasAsia.append(country.text)
            elif continent.text == "유럽":
                overseasEU.append(country.text)
            elif continent.text == "미주":
                overseasAmerica.append(country.text)    
            elif continent.text == "중동/아프리카":
                overseasAfrica.append(country.text)      
                
        for x in range(len(overseasAsia)):
            overseasAsiad[x+1] = overseasAsia[x]    
            
        for x in range(len(overseasEU)):
            overseasEUd[x+1] = overseasEU[x] 
            
        for x in range(len(overseasAmerica)):
            overseasAmericad[x+1] = overseasAmerica[x]     
            
        for x in range(len(overseasAfrica)):
            overseasAfricad[x+1] = overseasAfrica[x]      
            
    def printAsia(self):
        for k,v in overseasAsiad.items():
            print(k,". ",v)    
        for k,v in overseasEUd.items():
            print(k,". ",v)    
        for k,v in overseasAmericad.items():
            print(k,". ",v)    
        for k,v in overseasAfricad.items():
            print(k,". ",v)        
            
            
#==============================================================================    
    