from com.uc.data.ResultViewer import ResultViewer
from com.uc.utils.ColorUtil import *
import csv


class CsvViewer(ResultViewer):

    def init(self):
        self.reportPath += '.csv'

    def ShowResult(self):
        self.init()
        csvfile = file(self.reportPath, 'w')
        try:
            writer = csv.writer(csvfile)
            for task in self.lineInfo:
                writer.writerow([task])
                writer.writerows(self.lineInfo[task])
                writer.writerow('')
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print(inred("Exception: {}".format(exc_value)))
            print(inred("#######STACK TRACE:"))
            traceback.print_tb(exc_traceback)
        finally:
            csvfile.close()
            print(inblue("view Report: file://%s" % self.reportPath))
        pass
