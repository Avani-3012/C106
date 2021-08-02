import csv
import numpy as np

def getDSource(data_path):
    coffeeInMl =[]
    sleepHours =[]
    with open(data_path)as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffeeInMl.append(float(row["Coffee in ml"]))
            sleepHours.append(float(row["sleep in hours"]))
    return{"x":sleepHours,"y": coffeeInMl}

def findC(dataSource):
    correlation = np.corrcoef(dataSource['x'],dataSource['y'])
    print(correlation)

def setup():
    data_path = 'cups of coffee vs hours of sleep.csv'
    dataSource =getDSource(data_path)
    findC(dataSource)

setup()