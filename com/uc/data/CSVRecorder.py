
import time
from com.uc.utils.ColorUtil import *
import traceback
from com.uc.conf import Conf
import csv
from com.uc.data.DataRecord  import DataRecord
import sys

class  CSVRecorder(DataRecord):

	def __init__(self):
		self.data = {}
		self.recordPath = '{}report-{}.csv'.format(Conf.REPORT_DIR, time.strftime('%Y%m%d%H%M')[2:])
		self.dataToWrite = []

	def onData(self, task, case, data):
		print inblue('onData: {}, {}, {}'.format(task, case, data))
		if not self.data.has_key(task):
			self.data[task] = {}
		if not self.data[task].has_key(case):
			self.data[task][case] = []
		self.data[task][case].append(data)

	def onComplete(self):
		self.saveData()
		pass

	def getRecordPath(self):
		return self.recordPath

	def loadData(self):
		pass

	def saveData(self):
		cvsfile = file('/opt/lampp/htdocs/test/test.csv', 'w')
		try:
			for task in self.data.keys():
				self.dataToWrite.append([task])
				result = self.data.get(task)
				for case in result:
					value = result.get(case)
					value.insert(0, case)
					self.dataToWrite.append(value)
			# print ingreen(self.dataToWrite[0])
			# print ingreen(self.dataToWrite[1])
			writer = csv.writer(cvsfile)
			writer.writerows(self.dataToWrite)
		except:
			exc_type, exc_value, exc_traceback = sys.exc_info()
			print inred("Exception: {}".format(exc_value))
			print inred("#######STACK TRACE:")
			traceback.print_tb(exc_traceback)
		finally:
			cvsfile.close()
			print inblue("view Record: file:///opt/lampp/htdocs/test/test.csv")
			print inblue("view Record: http://100.84.44.238//test/test.csv")


	def testWrite(self):
		list1 = ['1', '2', '3', '4', '5']
		list2 = ['5', '6', '7', '8', '9']
		dic = {'a': list1, 'b': list2}
		listall = [list1, list2]
		cvsfile = file('/opt/test.csv', 'w')
		writer = csv.writer(cvsfile)
		# writer.writeheader()
		# writer.writerow(['a'] + list1)
		# writer.writerow(['b'] + list2)
		writer.writerows(listall)
