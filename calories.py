import re
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date

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
            activitiesDict[activityName].append((minSpeed, maxSpeed, eqSpeed, slope))
    else:   
        if row.__contains__('mph'):
            activitiesDict.update({activityName: [(minSpeed, maxSpeed, eqSpeed, slope)]})
        else:
            activitiesDict.update({activityName: slope})


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
            minSpeedKmh, maxSpeedKmh, eqSpeedKmh = convertMinMaxEqToKmh(minSpeedMph, maxSpeedMph, eqSpeedMph)
            
            #check conditions and add new sport activity to a dictionary
            addActivityToDict(activityName, activitiesDict, row, slope, minSpeedKmh, maxSpeedKmh, eqSpeedKmh)
                        
    return activitiesDict


def countBMR(sex, weight, height, age):
    match sex:
        case 'female':
            return 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
        case 'male':
            return 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
        case _:
            return None

def percentCaloriesInBMR(caloriesAmount, bmr):
    return caloriesAmount/bmr * 100

#structure of caloriesEaten: [(caloriesAmount, name of food)]
def pieChartWithCalories(caloriesEaten, bmr):
    #taking calories amounts and food names from a list of tuples
    caloriesAmounts = [percentCaloriesInBMR(elem[0], bmr) for elem in caloriesEaten]
    foodNames = [elem[1] for elem in caloriesEaten]

    #check if the eaten food exceeds 100%
    #if not, it will be showed in a pie chart
    sumCalories = sum(caloriesAmounts)
    if sumCalories < 100:
        unEatenPercent = 100 - sumCalories
        caloriesAmounts.append(unEatenPercent)
        foodNames.append('Not eaten')

    #set colours on a pie chart
    colours = sns.color_palette('bright')
    
    #set settings of a pie chart and percents to 2 decimal points
    plt.pie(caloriesAmounts, labels=foodNames, colors=colours, autopct= '%.2f%%')
    plt.show()


def findFoodNamesByString(listCalories, enteredString):
    listMatchingFoods = []
    
    #to remind, listCalories is of a structure: [(food name, food type, cal, kJ, g/ml)]
    for food in listCalories:
        #transform string to lowercase to avoid mis-match
        if enteredString.lower() in food[0].lower():
            listMatchingFoods.append(food)
    return listMatchingFoods


def findActivitiesByString(dictActivities, enteredString):
    dictMatchingActivities = dict()
    
    #to remind, dictActivities contains: {activityName: [(minSpeedKmh, maxSpeedKmh, eqSpeedKmh, slope)]} or {activityName: slope}
    for key, value in dictActivities.items():
        if enteredString.lower() in key.lower():
            dictMatchingActivities.update({key: value})
    return dictMatchingActivities
    
    
if __name__ == '__main__':
    #print(takeFirstNumberFromString(string))
    '''dict1 = loadActivitiesData()
    for item in dict1.items():
        print(item)'''
    dictActivities = {'Sledding, tobagganing, luge': 6.993062956504314, 'Cleaning gutters': 5.000084106353022, 
                     'Walking': [(None, 3.218688, None, 1.9929788501512924), (None, None, 3.218688, 2.495632807932813), 
                                (None, None, 4.02336, 2.998286765714334), (None, None, 4.828032, 3.298115442285767), 
                                (None, None, 5.632704, 3.827224871529473), (None, None, 5.632704, 5.996573531428668), 
                                (None, None, 6.437376, 5.000084106353022), (None, None, 7.2420480000000005, 6.2964022080001), 
                                (None, None, 8.04672, 8.02482634352954)]}
    print(findActivitiesByString(dictActivities, 'walk'))
    