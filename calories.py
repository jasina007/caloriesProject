import pandas as pd
import csv
import numpy as np
from sklearn.linear_model import LinearRegression








#convert lb value to kg
def convertLbToKg(lvValue):
    return 0.45359237 * lvValue

#all calories in every row in exercise_dataset.csv are in linear connection
#for this reason I count a slope of linear function with linear regression
def caloriesLinearRegression(valuesFromSmallestToGreatest):
    firstLb = convertLbToKg(130)
    secondLb = convertLbToKg(155)
    thirdLb = convertLbToKg(180)
    fourthLb = convertLbToKg(205)
    arguments = [[firstLb], [secondLb], [thirdLb], [fourthLb]]
    values = valuesFromSmallestToGreatest
    reg = LinearRegression().fit(arguments, values)
    print(reg.coef_)


if __name__ == '__main__':
    caloriesLinearRegression()

