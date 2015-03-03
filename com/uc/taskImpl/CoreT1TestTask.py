# encoding: utf-8

from time import sleep

from com.uc.conf import Conf
from com.uc.html.AverageTemplate import AverageTemplate
from com.uc.task.AbstractVideoTask import AbstractVideoTask
from com.uc.utils import BrowserUtils
from com.uc.html.DataStruct import DataStruct
from com.uc.utils.TaskLogger import TaskLogger


class CoreT1TestTask(AbstractVideoTask):
    urlList = Conf.CORE_T1_URL

    def __init__(self):
        super(CoreT1TestTask, self).__init__()
        # 设置过滤器
        self.setTemplate(AverageTemplate())
        self.setValueCount(1)
        self.setTitle(Conf.TASK_TYPE[0])

    def doTest(self):
        print("STARTUP UC")
        BrowserUtils.launchBrowser()

        sleep(Conf.WAIT_TIME)

        print("CLEAR HISTROY")
        BrowserUtils.clearVideoCache()

        TaskLogger.normalLog("PLAY VIDEO:")
        TaskLogger.detailLog(self.urlList[self.currentCategory])
        BrowserUtils.openURI(self.urlList[self.currentCategory])

        # 等待视频播起来
        myloop = 0
        while True:
            sleep(1)
            if self.hasStartPlay is True:
                TaskLogger.detailLog('play sucess')
                break
            elif myloop > 7:
                TaskLogger.errorLog('play time out')
                break
            myloop += 1

        BrowserUtils.openURIInCurrentWindow("http://www.baidu.com")

        sleep(Conf.WAIT_TIME)

        print("SHUTDOWN UC")
        BrowserUtils.closeBrowser()

    def onVideoFirstCoreT1(self, t1):
        self.dataRecord.onData(self.title, self.currentCategory, t1)
        if t1 <= 0:
            return
        self.getCurrentReultList().append(DataStruct(1, t1))

    def onPlayerVersion(self, version):
        self.setPlayerVersion(version)
        pass
