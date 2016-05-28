# -*- coding: utf-8 -*-
from xml.dom.minidom import parse,parseString
from xml.etree import ElementTree
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
import http.client
xmlFD = -1
BooksDoc = None
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

    def loadFromWeb(self):
        if self.conn == None:
            self.conn = HTTPConnection(self.fileName)
        url = self.userURIBuilder()
        print(url)
        
        self.conn.request("GET",url)
        self.req = self.conn.getresponse()
        print(self.req.status)
        if int(self.req.status) == 200:
           print("download Complete!")
        else:
           print("API Call Failed")
           return None
    #이거수정하기
   