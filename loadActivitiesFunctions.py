#here are functions used to loading activities data
import re
from sklearn.linear_model import LinearRegression

def convertLbToKg(lbValue):
    return 0.45359237 * lbValue

def convertMphToKmh(mphValue):
    return 1.609344 * mphValue

#convert all speeds to km/h
def convertMinMaxEqToKmh(minSpeedMph, maxSpeedMph, eqSpeedMph):
    if not minSpeedMph == None:
        minSpeedMph = convertMphToKmh(float(minSpeedMph))
    if not maxSpeedMph == None:
        maxSpeedMph = convertMphToKmh(float(maxSpeedMph))
    if not eqSpeedMph == None:
        eqSpeedMph = convertMphToKmh(float(eqSpeedMph))
    return minSpeedMph, maxSpeedMph, eqSpeedMph

#method which returns the first number from a string(both int and float) 
def takeFirstNumberFromString(string):
    listResult = takeAllNumbersFromString(string)
    if listResult:
        return listResult[0]
    return None

def takeAllNumbersFromString(string):
    searched = re.findall(r'\d*\.?\d+', string)
    listOfNumbers = []
    
    if searched:
        for num in searched:
            if '.' in num:
                num = float(num)
            else:
                num = int(num)
            listOfNumbers.append(num)
        return listOfNumbers
    return None
    
    
#returns how many numbers are in a string
def findHowManyNumbersAreInString(string):
    howMany = re.findall(r'\d*\.?\d+', string)
    return howMany.__len__()


#all calories in every row in exercise_dataset.csv are in linear connection
#for this reason, I count a slope of linear function with linear regression
def caloriesLinearRegression(valuesFromSmallestToGreatest):
    firstLb = convertLbToKg(130)
    secondLb = convertLbToKg(155)
    thirdLb = convertLbToKg(180)
    fourthLb = convertLbToKg(205)
    arguments = [[firstLb], [secondLb], [thirdLb], [fourthLb]]
    values = valuesFromSmallestToGreatest
    reg = LinearRegression().fit(arguments, values)
    return reg.coef_

def convert1DListTo2D(list1D):
    list2D = []
    for elem in list1D:
        list2D += [elem]
    return list2D

def makeListOfStringsToString(listOfStrings):
    stringResult = ""
    for string in listOfStrings:
        stringResult += f"{string} "
    return stringResult[:-1] #removing the last character(space)

#method to define speeds
def getMinMaxEqSpeedInRow(nameAndTypeActivity):
    minSpeedMph = None
    maxSpeedMph = None
    eqSpeedMph = None
    
    if nameAndTypeActivity.__contains__('mph'):
        if nameAndTypeActivity.__contains__( '(' ):
            eqSpeedMph = takeFirstNumberFromString(nameAndTypeActivity)
        else:
            howManyNumbers = findHowManyNumbersAreInString(nameAndTypeActivity)
            match howManyNumbers:
                case 1:
                    if nameAndTypeActivity.__contains__('<') or nameAndTypeActivity.__contains__('under'):
                        maxSpeedMph = takeFirstNumberFromString(nameAndTypeActivity)
                    elif nameAndTypeActivity.__contains__('>') or nameAndTypeActivity.__contains__('over'):
                        minSpeedMph = takeFirstNumberFromString(nameAndTypeActivity)
                    else:
                        eqSpeedMph = takeFirstNumberFromString(nameAndTypeActivity)
                case 2:
                    minSpeedMph,maxSpeedMph = takeAllNumbersFromString(nameAndTypeActivity)
                case _:
                    raise ValueError("Incorrect format of a row with speed values")
                                
    return minSpeedMph, maxSpeedMph, eqSpeedMph

#method which splits a row, giving a type and type of activity, giving speeds and calories amounts 
def splitRowAndGetData(row, signToSplit, indexToSplitRow, indexToSplitTypeActivity):
    splittedRow = re.split(signToSplit, row)
    nameAndTypeActivity = splittedRow[indexToSplitRow]
    minSpeedMph, maxSpeedMph, eqSpeedMph = getMinMaxEqSpeedInRow(nameAndTypeActivity)
    caloriesAmounts = splittedRow[indexToSplitTypeActivity]
    return nameAndTypeActivity, caloriesAmounts, minSpeedMph, maxSpeedMph, eqSpeedMph

def getActivityName(processedTypeActivity):
    if processedTypeActivity.__contains__('mph'):
        splittedActivityName = processedTypeActivity.split()
        activityName = makeListOfStringsToString(splittedActivityName[:-2])
    else:
        activityName = processedTypeActivity
    return activityName

def addActivityToDict(activityName, activitiesDict, row, slope, minSpeed, maxSpeed, eqSpeed):
    if activityName in activitiesDict:
        if row.__contains__('mph'):
            activitiesDict[activityName].append((minSpeed, maxSpeed, eqSpeed, slope))
    else:   
        if row.__contains__('mph'):
            activitiesDict.update({activityName: [(minSpeed, maxSpeed, eqSpeed, slope)]})
        else:
            activitiesDict.update({activityName: slope})