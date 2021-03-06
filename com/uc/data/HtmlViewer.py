from com.uc.data.ResultViewer import ResultViewer
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.data.TaskData import TaskData
from com.uc.conf import GConf
import sys
import traceback
import time


class HtmlViewer(ResultViewer):

    def __init__(self):
        self.data = {}
        self.dataCount = {}
        self.header = {}
        self.caseSeq = []
        # self.reportPath = '{}report.html'\
            # .format(GConf.getGlobal('REPORT_DIR'))
        self.reportPath = '%s%s-%s.html' % (GConf.getGlobal('REPORT_DIR'), GConf.getCase('RESULT_NAME'), time.strftime('%Y%m%d%H%M')[2:])
        self.templatepath = 'template/tableTemplate.html'

    def addData(self, data):
        taskInfo = {}
        self.data[str(data)] = taskInfo

        #  extra info
        extraData = ''
        extras = data.getAllExtra()
        for extra in extras:
            extraData = '%s %s %s' % (extraData, extra, extras[extra])
        taskInfo['extra'] = extras

        #  case data & head
        self.parseDataType(data, TaskData.DATA_TYPE_TIMING, taskInfo)
        self.parseDataType(data, TaskData.DATA_TYPE_NORMAL, taskInfo)
        pass

    def parseDataType(self, data, dataType, taskInfo):
        taskInfo[dataType] = []
        self.dataCount[dataType] = 0
        self.header[dataType] = []
        setHeader = False
        extraTemp = []
        for key in data.getKeysByType(dataType):
            caseData = data.getDataByTypeAndKey(dataType, key)
            lineContent = caseData.data[:]
            extras = data.getDataExtra(dataType, key)

            if not setHeader:
                for extra in extras:
                    self.header[dataType].append(extra)
                    extraTemp.insert(0, extra)
                setHeader = True

            count = len(lineContent)
            if count > self.dataCount[dataType]:
                self.dataCount[dataType] = count

            for extra in extraTemp:
                lineContent.insert(0, extras[extra])
            lineContent.insert(0, key)
            taskInfo[dataType].append(lineContent)

    def showResult(self, subPath=None):
        # self.init()
        htmlFile = file(self.reportPath, 'wb')
        templateFile = file(self.templatepath, 'rb')
        try:
            # use template
            htmlFile.write(templateFile.read())

            # write each task
            for taskInfo in self.data:
                self.writeTitle(htmlFile, taskInfo)
                self.writeExtra(htmlFile, self.data[taskInfo]['extra'])

                self.writeTableHead(htmlFile, self.dataCount[TaskData.DATA_TYPE_NORMAL], self.header[TaskData.DATA_TYPE_NORMAL])
                self.writeTableContent(htmlFile, self.data[taskInfo][TaskData.DATA_TYPE_NORMAL])
                self.writeTableHead(htmlFile, self.dataCount[TaskData.DATA_TYPE_TIMING], self.header[TaskData.DATA_TYPE_TIMING])
                self.writeTableContent(htmlFile, self.data[taskInfo][TaskData.DATA_TYPE_TIMING])
                self.writeTableEnd(htmlFile)
            if GConf.getCaseBool('RESULT_IMG') is True:
                TaskLogger.debugLog('do write img')
                self.writeImage(htmlFile, subPath)
            else:
                TaskLogger.debugLog('do not write img')
            self.writeTemplateEnd(htmlFile)
            return self.reportPath
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            TaskLogger.errorLog("Exception: {}".format(exc_value))
            TaskLogger.errorLog("#######STACK TRACE:")
            traceback.print_tb(exc_traceback)
        finally:
            htmlFile.close()
            templateFile.close()
            TaskLogger.detailLog("view Report: file://%s" % self.reportPath)
        pass

    def writeTitle(self, fileHandle, title):
        fileHandle.write("<h1>%s</h1>\n" % title)

    def writeExtra(self, fileHandle, extras):
        for extra in extras:
            temp = '%s: %s' % (extra, extras[extra])
            # TaskLogger.debugLog('extraData: %s , extra: %s, extras[extra]: %s' % (extraData, extra, extras[extra]))
            # extraData = '%s %s %s' % (extraData, extra, extras[extra])
            fileHandle.write("<p style=\"font-size: 20px\">%s</p>\n" % temp)
        fileHandle.write("\n")
        fileHandle.write("\n")

    def writeTableHead(self, fileHandle, length, prefix):
        # table head
        if length == 0:
            return
        extra = len(prefix)
        fileHandle.write("<table id=\'result_table\'>\n")
        fileHandle.write("<colgroup>\n")
        fileHandle.write("<col align=\'left\' />\n")
        fileHandle.write("<col align=\'right\' />\n")
        fileHandle.write("</colgroup>\n")
        fileHandle.write("<tr>\n")
        # fileHandle.write("<tr id=\'header_row\'>\n")
        # fileHandle.write("<td ></td>\n")
        # fileHandle.write("<td align = \"center\" colspan = '%s'>duration(ms)</td>\n" % str(length+extra))
        # fileHandle.write("</tr>\n")
        fileHandle.write("<tr class = \'passClass\'>\n")
        fileHandle.write("<td><strong>CASE</strong></td>\n")
        for i in range(0, extra):
            fileHandle.write("<td><strong>%s</strong></td>\n" % prefix[i])
        for j in range(0, length):
            fileHandle.write("<td><strong>%s</strong></td>\n" % str(j+1))
        fileHandle.write("</tr>\n")
        fileHandle.write("\n")

    def writeTableContent(self, fileHandle, content):
        # table content
        for oneline in content:
            fileHandle.write("<tr>\n")
            for item in oneline:
                fileHandle.write("<td>%s</td>\n" % item)
            fileHandle.write("</tr>\n")

    def writeTableEnd(self, fileHandle):
        fileHandle.write("</tr>\n")
        fileHandle.write("</table>\n")

    def writeImage(self, fileHandle, filePath):
        index = filePath.find(GConf.getGlobal('REPORT_DIR'))
        if index != -1:
            filePath = filePath[len(GConf.getGlobal('REPORT_DIR')):]
        fileHandle.write("<img src='%s'></img>" % filePath)

    def writeTemplateEnd(self, fileHandle):
        fileHandle.write("</body>\n")
        fileHandle.write("</html>\n")
        fileHandle.write("\n")
        fileHandle.write("\n")
        fileHandle.write("\n")

