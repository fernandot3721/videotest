# encoding: utf-8
'''
Created on 2015-1-21

@author: Administrator
'''
from com.uc.html.StyleTemplate import StyleTemplate

class AverageTemplate(StyleTemplate):
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
        
        for key in keys:
            datas = self.taskDataAdapt.getDatas(key)
            if  len(datas) <= 0:
                continue
            text += "<tr>"
            
            #包含的数据个数
            valueCount = datas[0].getDataCount()
            text += '''<td rowspan ="2"><b>''' + key + "</b></td>"
            
            for i in range(len(datas)):
                text += "<td colspan = \"" + str(valueCount) +"\">" + str(i)  + "</td>"
                
            text += "<td colspan = \"" + str(valueCount) +"\">平均</td>"
            text += "</tr>"
            
            text += "<tr>"
            mySum = [0] * valueCount
            for data in datas:
                for i in range(valueCount):
                    text += "<td>" + str(data.get(i)) + "</td>"
                    mySum[i] += data.get(i)
            
            #平均值
            for i in range(valueCount):
                text += "<td>"+ str(mySum[i]/max(1,len(datas))) + "</td>"
            
            
            text += "</tr>"
            
        return text
