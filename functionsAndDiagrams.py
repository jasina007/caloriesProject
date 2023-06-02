#in this file are methods creating diagrams and counting bmr and getting strings
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import json, os

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


#it is the way to sort a list with tuples with speeds
def findMinInSpeedTuple(tuple):
    smallest = float('inf')  # Infinity because every existing number is smaller than it
    
    # Iterate over the elements in the tuple(without the last one, slope)
    for element in tuple[:3]:
        if element is not None and element < smallest:
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


def loadDailyCaloriesFromFile():
    fileName = 'dailyCalories.json'
    
    #check if a file exists and is not empty
    if os.path.exists(fileName) and os.path.getsize(fileName) > 0:
        with open(fileName, 'r') as fileRead:
            caloriesDict = json.load(fileRead)
        return caloriesDict
    return None
    
def barDiagramWithDailyCalories(bmr):
    #loading data from JSON file
    dailyCaloriesAmount = loadDailyCaloriesFromFile()
    
    #plot a diagram only if file exists and is not empty
    if dailyCaloriesAmount is not None:
        arguments = dailyCaloriesAmount.keys()
        values = dailyCaloriesAmount.values()
        
        #plot the bar diagram
        plt.bar(arguments, values, color='red', width=0.35)
        #dashed line showes a BMR of user
        plt.axhline(y=bmr, label='BMR',color='black', linestyle='dashed')
        plt.legend() #to show what means a dashed line
        plt.xlabel('Date')
        plt.ylabel('Calories')
        plt.title('Eaten calories per day')
        plt.show()
        
        
def loadOnlyTodayCalories():
    fileName = 'dailyCalories.json'
    
    #load calories amount only if file exists and is not empty
    if os.path.exists(fileName) and os.path.getsize(fileName) > 0:
        with open(fileName, 'r') as fileRead:
            caloriesDict = json.load(fileRead)
        currentDateStr = str(datetime.now().date())
        if currentDateStr in caloriesDict.keys():
            return caloriesDict[currentDateStr]
        
    return None
            

if __name__ == '__main__':
    '''dictActivities = [(None, 3.218688, None, 1.9929788501512924), (None, None, 3.218688, 2.495632807932813), (None, None, 4.02336, 2.998286765714334), (None, None, 4.828032, 3.298115442285767), (None, None, 5.632704, 3.827224871529473), (None, None, 5.632704, 5.996573531428668), (None, None, 6.437376, 5.000084106353022), (None, None, 7.2420480000000005, 6.2964022080001), (None, None, 8.04672, 8.02482634352954)]
    print(getSlopeFromCorrectSpeedInterval(dictActivities, 3.4))'''
    saveTodayCaloriesToFile(2694)
