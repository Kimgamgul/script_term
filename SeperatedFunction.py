# -*- coding: utf-8 -*-
from xml.dom.minidom import parse,parseString
from xml.etree import ElementTree

xmlFD = -1
BooksDoc = None
class Functions:
    #이 함수는 파일에서 불러오기용
    def __init__(self,loadType,Name):
        #loadType 은 파일에서 읽어오는지 인터넷에서 불러오는지 여부 
        #인자를 이용하여 함수내부에서 불러올 인자를 설정할 수 있다.
        self.loadType = loadType
        #name은 파일이 있다면 불러올때 사용
        #서버랑 연결된다면 서버주소로 사용한다.
        self.Name = Name
    #이 함수는 openApi에서 접근하기용
    def __init__(self,loadType,Name,regKey,**items):
        self.__init__(self,loadType,Name)
        self.conn = None
        #두개는 생성자 오버로딩으로 regkey가 있다면
        #reg키를 넣는다.
        self.regKey = regKey
        #openAPI에서 필요한 URL을 만들기 위해서 diction형태로 초기화할때 넣어준다.
        self.items = items
    def userURIBuilder(self):
        str = "http://"+self.Name + "/serach"+"?"
        for key in self.items.keys():
            str += key + "=" + user[key] + "&"
        return str
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
            self.conn = HTTPConnection(self.Name)
        url = userURIBuilder()
        self.conn.request("GET",url)
        req = self.conn.getresponse()
        print(req.status)
        if int(req.status) == 200:
            print("download Complete!")
        else:
            print("API Call Failed")
            return None
            
    def loadFromExcel(self):
        
    def loadData(self):
        #여기서 데이터를 읽어옴
        #loadType으로 비교해서 File 이면 LoadFromFile,OpenApi면 LoadFromWeb함수호출
        