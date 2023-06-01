#in this file is a method which loading calories data from csv file
import re

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


    
if __name__ == '__main__':
    print(loadCaloriesData())
    
    
    