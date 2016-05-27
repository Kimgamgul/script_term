# -*- coding: utf-8 -*-
from xml.dom.minidom import parse
from http.client import HTTPConnection

##global
conn = None

class Functions:
    def __init__(self,Name,regKey):
        self.Name = Name
      
        #두개는 생성자 오버로딩으로 regkey가 있다면
        #reg키를 넣는다.
        self.regKey = regKey
        #openAPI에서 필요한 URL을 만들기 위해서 diction형태로 초기화할때 넣어준다.
    def userURIBuilder(self):
        str = "http://"+ self.Name + self.regKey
        return str
        
    def connectOpenAPIServer(self):
        global conn
        conn = HTTPConnection(self.Name)
        
    def loadFromWeb(self):
        if conn == None:
            self.connectOpenAPIServer()
        url = self.userURIBuilder()
        conn.request("GET",url)
        req = conn.getresponse()
        print(req.status)
        if int(req.status) == 200:
            print("download Complete!")
        else:
            print("API Call Failed")
            return None
            
