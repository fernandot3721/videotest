import matplotlib.pyplot as plt
import numpy as np
import math
from com.uc.utils.TaskLogger import TaskLogger


def createChrat(path, data, seq, row, col):

    i = 0
    plt.suptitle(path)
    for index in range(len(seq)):
        case = seq[index]
        i += 1
        dataA, dataB = data[case]
        a = map(float, dataA[1])
        b = map(float, dataB[1])
        # TaskLogger.debugLog('case: %s, 1:%s, 2:%s' % (case, dataA[0], dataB[0]))

        plt.subplot(row, col, i)
        plt.plot(a, label=dataA[0], color='red')
        plt.plot(b, label=dataB[0], color='green')
        plt.legend(fontsize=5, loc=0)
        plt.grid(True, color='0.8', linestyle='-')
        ax = plt.gca()
        maxValue = int(math.ceil((max(max(a), max(b))/10)))*10
        minValue = int(math.floor((min(min(a), min(b))/10)))*10
        # TaskLogger.debugLog("max: %s, min:%s" % (maxValue, minValue))
        ax.set_yticks(np.linspace(minValue, maxValue, 5))

        plt.xlabel("Count(per 5s)", fontsize='x-small')
        plt.ylabel("Memory(MB)", fontsize='x-small')
        plt.title(case)

    plt.subplots_adjust(wspace=0.4, hspace=1)
    plt.savefig(path, dpi=200, format='svg')
    pass
