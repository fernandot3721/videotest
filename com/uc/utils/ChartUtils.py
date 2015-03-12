from pygooglechart import SimpleLineChart
from pygooglechart import Axis
from pygooglechart import Chart
from com.uc.utils.TaskLogger import TaskLogger


def memstr2list(string):
    # convert str to list type & ignore char "\n"
    templist = string[:-1].split(",")

    for i in range(len(templist)):
        if i > 0:
            templist[i] = int(templist[i])
    return templist


def getinfolist(path):
    with open(path) as file:
        ret = list(map(list, zip(*map(memstr2list, file.readlines()))))
        print(ret)
        return ret


def createstripeschart(picpath, title, timelist, infolist):

    INTERVAL = 100

    a, b = infolist
    memfreelist = map(float, a)
    usslist = map(float, b)

    datalist = memfreelist+usslist

    # set max & min line for axis Y
    max_y = (int(max(datalist)/INTERVAL)+1)*INTERVAL
    min_y = (int(min(datalist)/INTERVAL)-1)*INTERVAL

    # Chart size of 704x396 pixels and specifying the range for the Y axis
    chart = SimpleLineChart(800, 375, y_range=[min_y, max_y])

    # Add the chart data
    chart.add_data(memfreelist)
    chart.add_data(usslist)
    # chart.set_legend(['INTELLIGENCE', 'INSANITY OF STATEMENTS'])

    # Set the line colour to blue
    chart.set_colours(['E6DB6C', '272822', '0000FF'])

    # Set the vertical stripes
    chart.fill_linear_gradient(Chart.CHART, 0, '272822', 0.2, '000000', 0.1)
    # Set the horizontal dotted lines
    chart.set_grid(len(timelist), INTERVAL*100/(max_y-min_y+1))

    # Y axis labels
    left_axis = list(range(min_y, max_y + 1, INTERVAL))
    chart.set_axis_labels(Axis.LEFT, left_axis)

    # X axis labels
    chart.set_axis_labels(Axis.BOTTOM, timelist)

    chart.set_line_style(0, 3)
    chart.set_title(title)
    chart.set_title_style(font_size=28)

    chart.download(picpath)
