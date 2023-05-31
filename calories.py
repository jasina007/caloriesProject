import re
from sklearn.linear_model import LinearRegression
import numpy as np

def splitAndConvertToInt(listOfSplittedRow, rowIndex):
    return int(re.split(' ', listOfSplittedRow[rowIndex])[0])
    
    
#data about calories are in order: (food name, food type, cal, kJ, g/ml)
def loadCaloriesData():
    caloriesList = []
    
    #getting all calories data from an opened file
    with open("calories.csv", 'r') as caloriesFile:
        next(caloriesFile) #skipping the first row(because there are names of columns)     
        for row in caloriesFile:
            commaSplittedRow = re.split(r',' , row) #splitting row by comma
            #there are 3 situations: quote around a food type[a]; food name[b] ; a lack of quote[c]
            #inside a quote may be only 1 comma  
      
            #situation [a]
            if commaSplittedRow[0].__contains__(r'"'): 
                typeFood = re.sub('"', '',  f"{commaSplittedRow[0]}, {commaSplittedRow[1]}")
                nameFood = commaSplittedRow[2]
            #situation [b]
            elif commaSplittedRow[2].__contains__(r'"'):
                typeFood = commaSplittedRow[0]
                nameFood = re.sub('"', '', f"{commaSplittedRow[1]}, {commaSplittedRow[2]}")
            #situation [c]
            else:    
                typeFood = commaSplittedRow[0]
                nameFood = commaSplittedRow[1]
    
            #check, what type of unit is that food(solid or liquid)
            if commaSplittedRow[-3].__contains__('g'):
                unit = 'grammes'
            else:
                unit = 'mililitres'
            
            #convertion of string amounts of calories and kilojoules into int type(reject 'cal' and 'kJ' suffixes)
            caloriesAmount = splitAndConvertToInt(commaSplittedRow, -2)
            kilojoulesAmount = splitAndConvertToInt(commaSplittedRow, -1)
            
            #add new tuple to list
            caloriesList.append((nameFood, typeFood, caloriesAmount, kilojoulesAmount, unit))
    return caloriesList #returning a created list of tuples

#below functions are a part of 'loadActivitiesData()' (to avoid repeating the same code and improve the readiness)

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
            activitiesDict[activityName].append([(minSpeed, maxSpeed, eqSpeed, slope)])
    else:   
        if row.__contains__('mph'):
            activitiesDict.update({activityName: [(minSpeed, maxSpeed, eqSpeed, slope)]})
        else:
            activitiesDict.update({activityName: [(slope)]})


#method which load 'exercise_dataset.csv' file and process data 
def loadActivitiesData():
    activitiesDict = dict()
    #getting all data about sport activities from opened file
    with open('exercise_dataset.csv', 'r') as activitiesFile:
        next(activitiesFile) #skipping the first row(because there are names of columns)  
        for row in activitiesFile:
            if row.__contains__('"'):
                nameAndTypeActivity, caloriesAmounts, minSpeedMph, maxSpeedMph, eqSpeedMph = splitRowAndGetData(row, '"', 1, 2)

                #check existence of 'mph' in a row and define a correct activity name
                if nameAndTypeActivity.__contains__('mph'):
                    splittedTypeActivity = re.split(',', nameAndTypeActivity)
                    #when the first word contains 'mph', then an activity name will be different
                    activityName = getActivityName(splittedTypeActivity[0])
                else:
                    activityName = nameAndTypeActivity                         
            else:
                nameAndTypeActivity, caloriesAmounts, minSpeedMph, maxSpeedMph, eqSpeedMph = splitRowAndGetData(row, ',', 0, slice(1, None))
                activityName = getActivityName(nameAndTypeActivity)
                
            #taking all calories and count a slope('a' in linear function) 
            arguments = takeAllNumbersFromString(str(caloriesAmounts))[:-1]
            slope = float(caloriesLinearRegression(convert1DListTo2D(arguments)))   
            
            #convert all speeds to km/h       
            minSpeed, maxSpeed, eqSpeed = convertMinMaxEqToKmh(minSpeedMph, maxSpeedMph, eqSpeedMph)
            
            #check conditions and add new sport activity to a dictionary
            addActivityToDict(activityName, activitiesDict, row, slope, minSpeed, maxSpeed, eqSpeed)
                        
    return activitiesDict

if __name__ == '__main__':
    #print(takeFirstNumberFromString(string))
    dict1 = loadActivitiesData()
    for item in dict1.items():
        print(item)