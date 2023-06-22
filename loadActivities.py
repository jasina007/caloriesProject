import re
from loadActivitiesFunctions import convertMinMaxEqToKmh, takeAllNumbersFromString, caloriesLinearRegression, \
    convert1DListTo2D, splitRowAndGetData, getActivityName, addActivityToDict
from functionsAndDiagrams import getMaxSpeedInList


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


if __name__ == '__main__':
    dict1 = loadActivitiesData()
    lista = dict1['Walking']
    print(getMaxSpeedInList(lista)) 
    