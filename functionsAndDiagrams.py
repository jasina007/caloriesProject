#in this file are methods creating diagrams and counting bmr and getting strings
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import json, os, re
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def countBMR(sex, weight, height, age):
    match sex:
        case 'female':
            return 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
        case 'male':
            return 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
        case _:
            return None

def countCaloriesInFoodAmount(foodAmount, caloriesPer100gMl):
    return foodAmount/100 * caloriesPer100gMl

def percentCaloriesInBMR(caloriesAmount, bmr):
    return caloriesAmount/bmr * 100



def getEstimatingTimeSlope(slope, weight, caloriesAmount):
    try:
        hoursFloat = caloriesAmount/(weight*slope)
        hours = int(hoursFloat)
        minutes = (hoursFloat - hours)*60
        return (int(hours), int(minutes))
        
    except ValueError:
        print("Dividing by 0")


def getFoodNameFromRow(foodRow):
    splittedName = re.split(',', foodRow)[0]
    return re.sub(r'[\(\'\']', '', splittedName)

def correctValueFromString(stringActivity):
    withoutQuote = re.split("\'", stringActivity)[-1]
    first_comma_removed = withoutQuote.replace(',', '', 1)
    return first_comma_removed[:-1].replace(" ", "")


def listOrFloat(valueString):
    if valueString.startswith("[") and valueString.endswith("]"):
        return "list"
    else:
        return "float"


def getListFromListStringActivities(stringList):
    splitted = re.split("['']", stringList)[1:-1]
    return [item for item in splitted if len(item)>=3 ]
    
def convertListToListOfTuples(strList):
    return [tuple(item.split(',')) for item in strList]

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


#it is the way to sort a list with tuples with speeds
def findMinInSpeedTuple(tuple):
    smallest = float('inf')  # Infinity because every existing number is smaller than it
    
    # Iterate over the elements in the tuple(without the last one, slope)
    for element in tuple[:3]:
        if element is not None:
            if float(element) < smallest:
                smallest = element
    return smallest

# Sort the list of tuples based on the smallest number in each tuple(without slopes)
def sortSpeedValues(dictValueSpeed):
    sorted_data = sorted(dictValueSpeed, key=findMinInSpeedTuple)
    return sorted_data


#define what is a minimum speed what user can enter(by a widget)
def getMinSpeedEnteredByUser(listTupleSpeeds):
    sortedListSpeeds = sortSpeedValues(listTupleSpeeds)
    firstTupleSpeed = sortedListSpeeds[0]
    minSpeedTuple = findMinInSpeedTuple(firstTupleSpeed)
    indexMinSpeed = firstTupleSpeed.index(minSpeedTuple)
    
    #there are only 2 possibilities: maxSpeed(index == 1) or eqSpeed(index==2)
    match indexMinSpeed:
        case 2: 
            return minSpeedTuple
        case 1: 
            return 0
        case _:
            return None


#get a slope of a speed defined by a user from specified interval defined in activities data
def getSlopeFromCorrectSpeedInterval(listTupleSpeeds, speedKmh):
    sortedListSpeeds = sortSpeedValues(listTupleSpeeds)
    currentIndex = 1
    
    #check if a speed entered by user belongs to current interval, if not, index is increasing
    while(currentIndex < len(sortedListSpeeds)):
        if speedKmh < findMinInSpeedTuple(sortedListSpeeds[currentIndex]):
            return sortedListSpeeds[currentIndex-1][-1]
        currentIndex += 1
        
    #if a speed is bigger than all intervals, the returning slope is from the last tuple
    if currentIndex == len(sortedListSpeeds):
        return sortedListSpeeds[currentIndex-1][-1]
        

#save today's amount of calories to a file
#  there are 4 options: file doesn't exist[a]; file is empty(user deleted all data)[b]; 
#  file has previous dates, but not today's[c]; in a file is today's date(we want to overwrite item with current date)[d]
def saveTodayCaloriesToFile(caloriesTotalAmount):
    todayDateStr = str(datetime.now().date())
    fileName = 'dailyCalories.json'

    if os.path.exists(fileName) and os.path.getsize(fileName) > 0:
        with open(fileName, 'r') as fileRead:
            caloriesDict = json.load(fileRead)
        
        #[d] situation
        if todayDateStr in caloriesDict.keys():
            caloriesDict[todayDateStr] = caloriesTotalAmount
        else: #[c] situation
            caloriesDict.update({todayDateStr: caloriesTotalAmount})
    else: #[a] ; [b]
        caloriesDict = {todayDateStr: caloriesTotalAmount}
    
    #save updated dictionary to a file
    with open(fileName, 'w') as fileWrite:
        json.dump(caloriesDict, fileWrite)


def loadSthFromFile(filename):
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r') as fileRead:
            caloriesDict = json.load(fileRead)
        return caloriesDict
    return None


def loadDailyCaloriesFromFile():
    return loadSthFromFile('dailyCalories.json')
    
    
def loadOnlyTodayCalories():
    fileName = 'dailyCalories.json'
    
    #load calories amount only if file exists and is not empty
    if os.path.exists(fileName) and os.path.getsize(fileName) > 0:
        with open(fileName, 'r') as fileRead:
            caloriesDict = json.load(fileRead)
        currentDateStr = str(datetime.now().date())
        if currentDateStr in caloriesDict.keys():
            return caloriesDict[currentDateStr]
        
    return 0
    
    
def clearJsonDailyCalories():
    clearJsonFile('dailyCalories.json')

def clearJsonTodayEatings():
    clearJsonFile('todayEatings.json')
    
    
#method to clear a dailyCalories.json file        
def clearJsonFile(fileName):
    if os.path.exists(fileName):
        with open(fileName, 'w') as file:
            json.dump({}, file)
            
def saveTodayEatings(eatingsDictionary):
    filename = 'todayEatings.json'
    
    with open(filename, 'w') as file:
        json.dump(eatingsDictionary, file)
    
def loadTodayEatings():
    filename = 'todayEatings.json'
    return loadSthFromFile(filename)

if __name__ == '__main__':
    dictActivities = "['None,3.218688,None,1.9929788501512924', 'None,None,3.218688,2.495632807932813', 'None,None,4.02336,2.998286765714334', 'None,None,4.828032,3.298115442285767', 'None,None,5.632704,3.827224871529473', 'None,None,5.632704,5.996573531428668', 'None,None,6.437376,5.000084106353022', 'None,None,7.2420480000000005,6.2964022080001', 'None,None,8.04672,8.02482634352954']"
    '''print(getSlopeFromCorrectSpeedInterval(dictActivities, 0))
    print(getMinSpeedEnteredByUser(dictActivities))'''
    print(getMinSpeedEnteredByUser(convertListToListOfTuples(getListFromListStringActivities(dictActivities))))
