##################################
#### Created by Andrea Bena' #####
##################################

import sys
from math import sqrt


# BUS_ID=2187 | LINE_ID=13 | X_AXIS=10 | Y_AXIS=1003 | TIME=18000
# 2187 13 10 1003 18000
# 3002 4 5000 5 18100
# 2187 13 100 2030 18500
# 3002 4 5000 1100 18600
# 2187 13 300 3300 19200
# 3002 4 5000 2200 19200
# 1976 4 5000 5 18600
# 1976 4 5000 1100 19600
# 1976 4 5000 2200 20100

class BusRecord:
    def __init__(self, bus_id, line_id, x, y, time):
        self.bus_id = bus_id
        self.line_id = line_id
        self.x = x
        self.y = y
        self.time = time


def load_data(file_name, target):
    try:
        data = []
        with open(file_name, 'r') as f:
            for line in f:
                splitted = line.split()
                if target in splitted:
                    busId, lineId, x, y, time = splitted
                    data.append(BusRecord(busId, lineId, x, y, time))
        return data
    except:
        raise  # If we do not provide an exception, the current exception is propagated


def euclidean_distance(el1, el2):
    return sqrt((int(el1.x) - int(el2.x)) ** 2 + (int(el1.y) - int(el2.y)) ** 2)


def calc_total_distance(records):
    distance = 0
    for el1, el2 in zip(records[:-1], records[1:]):
        distance += euclidean_distance(el1, el2)
    return distance


def get_total_distance(records):
    # Check the len of load_records, must be greater than 1
    return round(calc_total_distance(records), 2)


def get_average_speed(records):
    speed = 0.0
    ids = []
    records = sorted(sorted(records, key=lambda t: t.time)[::-1], key=lambda b: b.bus_id)

    for el in records:
        if el.bus_id not in ids:
            ids.append(el.bus_id)

    for id in ids:
        for el1, el2 in zip(records[:-1], records[1:]):
            if el1.bus_id == el2.bus_id and el1.bus_id == id:
                distance = euclidean_distance(el1, el2)
                time = float(el1.time) - float(el2.time)
                speed += distance / time
            else:
                continue

    return round(speed / (len(records) - 1), 2)


if __name__ == '__main__':
    # flag is ’-b’, parameter is busId. Program print total distance traveled by the given bus
    # flag is ’-l’, parameter is lineId. Program print average speed of buses traveling on the line
    if len(sys.argv) != 4:
        print("Error!! Syntax usage: %s <input_file.txt> <parameter> <input_value>" % sys.argv[0])
        print("Parameters:\n-b: show the total distance traveled by busId\t\t\n input value: busId\n"
              "-t: show the average speed of buses travelling on the line\t\t\n input value: lineId\n")
        exit(0)

    records = load_data(sys.argv[1], sys.argv[3])
    if records == 1:
        print("The number of record must be greater than one!!")
        exit(-1)

    if sys.argv[2] == '-b':
        print('\nBus id = %s - Total Distance:' % sys.argv[3], get_total_distance(records), "m")
    elif sys.argv[2] == '-l':
        print('\nLine id = %s - Avg Speed:' % sys.argv[3], get_average_speed(records), "m/s")
    else:
        raise KeyError()
