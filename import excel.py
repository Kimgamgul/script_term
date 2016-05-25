# -*- coding: utf-8 -*-
import win32com.client

x = 3
number_dict = dict()
num = 0

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
wb = excel.Workbooks.Open('C:\\Users\\user\\Downloads\\trip\\wifi.xlsx')
ws = wb.ActiveSheet

while(ws.Cells(x,2).Value != None):
    if ws.Cells(x,2).Value in number_dict.keys():
       pass 
    else:
        num+=1
        number_dict[num] += ws.Cells(x,2).Value
       
    x+=1
    
    

for k,v in number_dict.items():
    print(k,". ",v)
    
excel.Quit()