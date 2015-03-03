from com.uc.data.ResultViewer import ResultViewer
from com.uc.utils.TaskLogger import TaskLogger
from com.uc.conf import Conf
import sys
import traceback
import time


class HtmlViewer(ResultViewer):

    def __init__(self):
        self.dataCount = 0
        self.data = {}
        # self.reportPath = '{}report.html'\
            # .format(Conf.REPORT_DIR)
        self.reportPath = '{}report-{}.html'\
            .format(Conf.REPORT_DIR, time.strftime('%Y%m%d%H%M')[2:])
        self.templatepath = Conf.HTML_TEMPLATE

    def addData(self, data):
        taskInfo = {}
        self.data[str(data)] = taskInfo

        #  extra info
        extraData = ''
        extras = data.getAllExtra()
        for extra in extras:
            extraData = '%s %s %s' % (extraData, extra, extras[extra])
        taskInfo['extra'] = extraData

        #  case data & head
        self.dataCount = 0
        taskInfo['case'] = []
        for case in data.getCase():
            lineContent = data.getData(case)
            count = len(lineContent)
            if count > self.dataCount:
                self.dataCount = count

            caseExtras = data.getCaseExtra(case)
            lineContent.insert(0, caseExtras['AVG'])
            lineContent.insert(0, case)
            taskInfo['case'].append(lineContent)
        pass

    def showResult(self):
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

                self.writeTableHead(htmlFile, self.dataCount, ['case', 'AVG'])
                self.writeTableContent(htmlFile, self.data[taskInfo]['case'])
                self.writeTableEnd(htmlFile)
            self.writeTemplateEnd(htmlFile)
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

    def writeExtra(self, fileHandle, extra):
        TaskLogger.debugLog("=============%s" % extra)
        fileHandle.write("<p>%s</p>\n" % extra)
        fileHandle.write("\n")
        fileHandle.write("\n")

    def writeTableHead(self, fileHandle, length, prefix):
        # table head
        extra = len(prefix)
        fileHandle.write("<table id=\'result_table\'>\n")
        fileHandle.write("<colgroup>\n")
        fileHandle.write("<col align=\'left\' />\n")
        fileHandle.write("<col align=\'right\' />\n")
        fileHandle.write("</colgroup>\n")
        fileHandle.write("<tr>\n")
        fileHandle.write("<tr id=\'header_row\'>\n")
        fileHandle.write("<td ></td>\n")
        fileHandle.write("<td align = \"center\" colspan = '%s'>duration(ms)</td>\n" % str(length+extra))
        fileHandle.write("</tr>\n")
        fileHandle.write("<tr class = \'passClass\'>\n")
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
        fileHandle.write("</table>\n")

    def writeTemplateEnd(self, fileHandle):
        fileHandle.write("</body>\n")
        fileHandle.write("</html>\n")
        fileHandle.write("\n")
        fileHandle.write("\n")
        fileHandle.write("\n")

