import math
from turtle import right
import matplotlib.pyplot as plt
import json


def main():
    data = LoadData('data/7_2/data2.json')

    isLinear = False
    if(isLinear):
        rxy = LinearCorrelationCoeff(data)
        print("Значение коэффициента корреляции: " + str(round(rxy, 4)))
    else:
        rs = RangCorrelationCoeff(data)
        print("Значение коэффициента корреляции: " + str(round(rs[0], 4)))
        print("Значение t_расч: " + str(round(rs[1], 4)))

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

def CalcRank(index, count):
    left = (index+count)*((index+count)+1)/2
    right = (index-1)*(index)/2
    return (left-right)/(count+1)

def GetRankedList(list):
    seq = sorted(list)
    return [CalcRank(seq.index(v)+1, list.count(v)-1) for v in list]

def RangCorrelationCoeff(data):
    x_data_ranks = GetRankedList(list(zip(*data))[0])
    y_data_ranks = GetRankedList(list(zip(*data))[1])
    print("x_data_ranks: " + str(x_data_ranks))
    print("y_data_ranks: " + str(y_data_ranks))

    di = []
    di2 = []
    for i in range(len(data)):
        di_item = x_data_ranks[i] - y_data_ranks[i]
        di.append(di_item)
        di2.append(di_item*di_item)
    
    print("di: " + str(di) + " Сумма " + str(sum(di)))
    print("di^2: " + str(di2) + " Сумма " + str(sum(di2)))
    
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