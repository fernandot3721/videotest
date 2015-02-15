# encoding: utf-8
'''
Created on 2015-1-21

@author: Administrator
'''
from com.uc.html.StyleTemplate import StyleTemplate

class ScaleTemplate(StyleTemplate):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        StyleTemplate.__init__(self)
    def createReportb(self):
        text = '''<table border="1">'''
        text += "<caption><H1>" + self.taskDataAdapt.getTitle() + "</H1></caption>"
        
        keys = sorted(self.taskDataAdapt.getKeys())
        statDatas = {}
        for key in keys:
            datas = self.taskDataAdapt.getDatas(key)
            if datas is None:
                continue     
            valueCount = datas[0].getDataCount()
            for data in datas:
                for i in range(valueCount):
                    if statDatas.has_key(data.get(i)):
                        statDatas[data.get(i)] =  statDatas[data.get(i)] + 1
                    else :
                        #statDatas.setdefault(data.get(i),default=1)
                        statDatas[data.get(i)] =  1
        text += "<tr><td ><b> result </b></td>" + "<td>count</td><td>scale</td></tr>"
        mySum = 0
        for value in statDatas.values():
            mySum +=value
            
        for (key,value) in statDatas.items():
            text += "<tr>"
            text += '''<td ><b>''' + str(key) + "</b></td>"
            text += "<td>" + str(value) + "</td>"  
            text += "<td>" + str((float(value)/mySum)*100) + "</td>"  
            text += "</tr>"               
        
        return text
