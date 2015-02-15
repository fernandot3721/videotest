# encoding: utf-8
'''
Created on 2015-1-21

@author: Administrator
'''
from com.uc.html.HtmlNode import HtmlNode


class HtmlBuilder:
    nodeList = []
    
    def addNode(self,node):
        self.nodeList.append(node)
    
    def generatingRepors(self):
        text = ""
        text += self.generatingbefore()
        
        for node in self.nodeList:
            try:
                text += node.createHtmlCode()
            except Exception as e:
                print e
        
        text += self.generatingafter()
        
        return text
        
    def generatingbefore(self):
        return '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><title>视频测试报表</title>'''
    
    def generatingafter(self):
        return "</body></Html>"