import math
import matplotlib.pyplot as plt
import json


def main():
    data = LoadData('data/data2_1.json')
    rxy = LinearCorrelationCoeff(data)

    print(rxy)
    ShowCorrelationPlot(data)


def FindAvarge(data, column_num):
    avg = 0
    column = list(zip(*data))[column_num]
    avg = sum(column) / len(data)

    return avg

def LinearCorrelationCoeff(data):
    avg_x = FindAvarge(data, 0)
    avg_y = FindAvarge(data, 1)

    xMinAvg2Sum = 0
    yMinAvg2Sum = 0
    numerator = 0
    denominator = 0

    for item in data:
        xMinAvg = (item[0] - avg_x)
        yMinAvg = (item[1] - avg_y)

        numerator += xMinAvg*yMinAvg

        xMinAvg2Sum += xMinAvg * xMinAvg
        yMinAvg2Sum += yMinAvg * yMinAvg

    denominator = math.sqrt(xMinAvg2Sum*yMinAvg2Sum)

    return numerator/denominator

def RangCorrelationCoeff(data):
    di2 = []

    for item in data:
        di = item[0] - item[1]
        di2.append(di*di)

    n = len(data)
    rs = 1 - (6*sum(di2)) / (n * (n*n - 1))
    t_calc = abs(rs)*math.sqrt((n-2)/(1-rs*rs))
    return (rs, t_calc)

def ShowCorrelationPlot(data):
    x_data = list(zip(*data))[0]
    y_data = list(zip(*data))[1]

    max_value = max(max(x_data), max(y_data))

    plt.plot(x_data, y_data, 'ro')
    plt.axis([0, max_value*1.2, 0, max_value*1.2])
    plt.show()


def LoadData(path):
    f = open(path)
    data = json.load(f)
    f.close()

    return data

main()