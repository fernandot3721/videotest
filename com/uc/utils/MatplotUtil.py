import matplotlib.pyplot as plt
import numpy as np
import math
from com.uc.utils.TaskLogger import TaskLogger

PLOT_COLOR = [
    'red',
    'green',
    'blue',
    'cyan',
    'yellow',
    'magenta',
    'black'
]


def createChrat(path, data, seq, row, col):
    '''
        path: location to save the chart and also the title
        data: data to generate charts
        seq: sequence of the charts
        row: rows for layout
        col: colums for layot
        note: it requires data includes two task with same name
            eg: two hd_local_uss with 2.1.1 and 2.1.0 etc
    '''

    lineCount = len(seq)
    rowCount = int(math.ceil(float(lineCount)/col))
    if rowCount > row:
        row = rowCount

    lengh = 4 * col
    heigh = 1.8 * row

    plt.figure(figsize=(lengh, heigh))
    plt.suptitle(path)
    # TaskLogger.debugLog('lineCount: %s' % lineCount)
    for index in range(lineCount):
        case = seq[index]

        caseCount = len(data[case])
        if caseCount > 7:
            raise Exception("too many lines to draw")

        # TaskLogger.debugLog('draw %s row, %s col, %s' % (row, col, index))
        plt.subplot(row, col, index+1)

        maxValue = 0.0
        minValue = 9999.9
        for j in range(caseCount):
            sample = data[case][j]
            floatSample = map(float, sample[1])
            plt.plot(floatSample, label=sample[0], color=PLOT_COLOR[j])
            maxValue = int(math.ceil((max(max(floatSample), maxValue)/10)))*10
            minValue = int(math.floor((min(min(floatSample), minValue)/10)))*10

        plt.legend(fontsize=5, loc=0)
        plt.grid(True, color='0.8', linestyle='-')
        ax = plt.gca()
        ax.set_yticks(np.linspace(minValue, maxValue, 5))

        plt.title(case, fontsize=10)

    plt.subplots_adjust(wspace=0.4, hspace=1)
    plt.savefig(path, dpi=400, format='svg')
    pass
