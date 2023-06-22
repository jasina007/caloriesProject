import sys,re, ast
from datetime import datetime
from PySide6.QtCore import (QRect, QTimer, Qt)
from PySide6.QtGui import QPen, QPainter

from PySide6.QtWidgets import (QApplication, QComboBox, 
                               QHBoxLayout,QLabel, QLineEdit, 
                               QListWidget, QListWidgetItem,QMainWindow, 
                               QPushButton, QStatusBar,
                                QVBoxLayout, QWidget, QMessageBox, QSlider)
from PySide6.QtCharts import QChart, QPieSeries, QChartView, QBarSeries, QBarSet, QBarCategoryAxis, QValueAxis, QLineSeries
from loadCalories import loadCaloriesData
from loadActivities import loadActivitiesData
from functionsAndDiagrams import (findFoodNamesByString, countBMR, countCaloriesInFoodAmount, percentCaloriesInBMR, 
                                  loadOnlyTodayCalories, saveTodayCaloriesToFile, getFoodNameFromRow,
                                  loadDailyCaloriesFromFile, clearJsonTodayEatings, clearJsonDailyCalories,
                                  loadTodayEatings, saveTodayEatings, findActivitiesByString, correctValueFromString,
                                  listOrFloat, getListFromListStringActivities, getMinSpeedEnteredByUser,
                                  convertListToListOfTuples, getSlopeFromCorrectSpeedInterval,
                                  getEstimatingTimeSlope, getMaxSpeedInList)
from loadActivitiesFunctions import takeFirstNumberFromString


class FoodMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1445, 677)
        self.setWindowTitle("Food types window")
        self.centralwidget = QWidget()
        
        #there are 2 data layouts types: with vertical layout only and with horizontal layout inside a vertical layout
        #sex layout
        self.sexLayoutWidget = QWidget(self.centralwidget)
        self.sexLayoutWidget.setGeometry(QRect(19, 10, 81, 51))
        self.sexComboBoxWidget = QComboBox(self.sexLayoutWidget)
        self.sexComboBoxWidget.addItem("Female")
        self.sexComboBoxWidget.addItem("Male")
        self.sexLayout = self.userDataWithoutUnit("Sex", self.sexComboBoxWidget, self.sexLayoutWidget)
        
        #height layout
        self.heightLayout, self.heightLayoutWidget, self.heightWidget = self.userDataWithUnitLayout(QRect(140, 10, 91, 51), "Height", "cm")

        #weight layout
        self.weightLayout, self.weightLayoutWidget, self.weightWidget = self.userDataWithUnitLayout(QRect(270, 10, 91, 51), "Weight", "kg")

        #age layout
        self.ageLayout, self.ageLayoutWidget, self.ageWidget = self.userDataWithUnitLayout(QRect(400, 10, 112, 51), "Age", "years old")

        #food layout
        foodLayoutWidget = QWidget(self.centralwidget)
        foodLayoutWidget.setGeometry(QRect(550, 10, 211, 51))
        self.foodWidget = QLineEdit(foodLayoutWidget)
        self.foodLayout = self.userDataWithoutUnit("Food", self.foodWidget, foodLayoutWidget)

        #food amount layout
        self.foodAmountLayout, self.foodAmountLayoutWidget, self.foodAmountWidget = self.userDataWithUnitLayout(QRect(800, 10, 111, 51), 
                                                                                                                "Food amount", "g/ml")

        #confirm data button
        self.confirmDataButton = self.createPushButton(QRect(130, 80, 91, 24), "Confirm data")
        self.confirmDataButton.clicked.connect(self.loadFoodTypesAndSearch)
        
        
        #food list layout        
        self.foodListLayout, self.foodListLayoutWidget, self.foodListWidget = self.createFoodListLayout()

        #BMR data layout
        self.bmrLayout, self.bmrLayoutWidget, self.circleDiagramChartView, self.countBmrFunctionLabel, \
            self.countAmountCaloriesLabel, self.percentBmrFunctionLabel = self.createBmrInfoLayout()

        #bottom buttons
        self.sportActivityButton = self.createPushButton(QRect(800, 610, 111, 41), "Sport activity")
        self.resetFoodButton = self.createPushButton(QRect(20, 610, 121, 41), "Reset foods")

        #variables getting to know if a diagram bar is created(and axis on it)
        self.xAxisAttached = False
        self.yAxisAttached = False

        #daily calories layout
        self.dailyCaloriesLayout, self.dailyCaloriesLayoutWidget, self.barFoodDiagramChartView = self.createDailyCalories()
        
        self.resetFoodsShows = False
        
        #deactivate most layouts at start of the app
        self.deactivateAtStart()
        
        #total amount of calories of this day 
        self.todayCaloriesAmount = loadOnlyTodayCalories()
        
        #initializing of a dictionary with different food names and calories amount, necessary to diagrams
        #structure of this dict: {food name: caloriesAmount}
        self.todayDifferentFoodsDict = loadTodayEatings()
        
        #set status bar and central widget
        self.setCentralWidget(self.centralwidget)
        self.statusBarSetting()
        
        #loading food types from a 'calories.csv' file
        try:
            self.caloriesList = loadCaloriesData()
        except FileNotFoundError:
            self.createAndPrintMessageBox("Lack of file", "There isn't a calories.csv file in a directory")


    #layout type with horizontal layout inside vertical layout
    def userDataWithUnitLayout(self, dimensions, dataTypeName, unitName):
        layoutWidget = QWidget(self.centralwidget)
        layoutWidget.setGeometry(dimensions)
        layout = QVBoxLayout(layoutWidget)
        layout.setContentsMargins(0, 0, 0, 0)
        label = QLabel(layoutWidget, text=dataTypeName)
        layout.addWidget(label)
        horizontalLayout = QHBoxLayout()
        lineEditWidget = QLineEdit(layoutWidget)
        horizontalLayout.addWidget(lineEditWidget)
        unitLabel = QLabel(layoutWidget, text=unitName)
        horizontalLayout.addWidget(unitLabel)
        layout.addLayout(horizontalLayout)
        return layout, layoutWidget, lineEditWidget
    
    
    #layout type without horizontal layout
    def userDataWithoutUnit(self, dataTypeName, dataWidget, layoutWidget):
        layout = QVBoxLayout(layoutWidget)
        layout.setContentsMargins(0, 0, 0, 0)
        label = QLabel(layoutWidget, text=dataTypeName)
        layout.addWidget(label)
        layout.addWidget(dataWidget)
        return layout
    
    
    def createFoodListLayout(self):
        foodListLayoutWidget = QWidget(self.centralwidget)
        foodListLayoutWidget.setGeometry(QRect(20, 120, 326, 271))
        foodListLayout = QVBoxLayout(foodListLayoutWidget)
        foodListLayout.setContentsMargins(0, 0, 0, 0)
        chooseFoodLabel = QLabel(foodListLayoutWidget, text="Choose kind of 'Food' (entered above):")
        foodListLayout.addWidget(chooseFoodLabel)
        columnsFoodLabel = QLabel(foodListLayoutWidget, text="Full name, Type, Calories per 100g/ml, Kilojoules per 100g/ml")
        foodListLayout.addWidget(columnsFoodLabel)
        foodListWidget = QListWidget(foodListLayoutWidget)
        foodListLayout.addWidget(foodListWidget)
        return foodListLayout, foodListLayoutWidget, foodListWidget
    
    
    def createBmrInfoLayout(self):
        bmrLayoutWidget = QWidget(self.centralwidget)
        bmrLayoutWidget.setGeometry(QRect(368, 90, 541, 301))
        bmrLayout = QVBoxLayout(bmrLayoutWidget)
        bmrLayout.setContentsMargins(0, 0, 0, 0)
        caloriesInfoLayout = QVBoxLayout()
        bmrHorizontalLayout = QHBoxLayout()
        bmrLabel = QLabel(bmrLayoutWidget, text="Basal Metabolic Rate")
        bmrHorizontalLayout.addWidget(bmrLabel)
        countBmrFunctionLabel = QLabel(bmrLayoutWidget)
        bmrHorizontalLayout.addWidget(countBmrFunctionLabel)
        calLabel = QLabel(bmrLayoutWidget, text="cal")
        bmrHorizontalLayout.addWidget(calLabel)
        caloriesInfoLayout.addLayout(bmrHorizontalLayout)
        foodCaloriesHorizontalLayout = QHBoxLayout()
        caloriesInfoLabel = QLabel(bmrLayoutWidget, text="Calories in chosen food in entered amount: ")
        foodCaloriesHorizontalLayout.addWidget(caloriesInfoLabel)
        countAmountCaloriesLabel = QLabel(bmrLayoutWidget)
        foodCaloriesHorizontalLayout.addWidget(countAmountCaloriesLabel)
        calLabel_2 = QLabel(bmrLayoutWidget, text="cal")
        foodCaloriesHorizontalLayout.addWidget(calLabel_2)
        caloriesInfoLayout.addLayout(foodCaloriesHorizontalLayout)
        percentHorizontalLayout = QHBoxLayout()
        bmrInfoLabel = QLabel(bmrLayoutWidget, text="Percentage amount of food calories in BMR: ")
        percentHorizontalLayout.addWidget(bmrInfoLabel)
        percentBmrFunctionLabel = QLabel(bmrLayoutWidget)
        percentHorizontalLayout.addWidget(percentBmrFunctionLabel)
        percentSignLabel = QLabel(bmrLayoutWidget, text="%")
        percentHorizontalLayout.addWidget(percentSignLabel)
        caloriesInfoLayout.addLayout(percentHorizontalLayout)
        circleDiagramInfoLabel = QLabel(bmrLayoutWidget, text="Circle diagram with all entered food types:")
        caloriesInfoLayout.addWidget(circleDiagramInfoLabel)
        circleDiagramChartView = QChartView(bmrLayoutWidget)
        caloriesInfoLayout.addWidget(circleDiagramChartView)
        bmrLayout.addLayout(caloriesInfoLayout)
        
        return bmrLayout, bmrLayoutWidget, circleDiagramChartView, countBmrFunctionLabel, \
            countAmountCaloriesLabel, percentBmrFunctionLabel
    
    
    def createDailyCalories(self):
        dailyCaloriesLayoutWidget = QWidget(self.centralwidget)
        dailyCaloriesLayoutWidget.setGeometry(QRect(20, 400, 891, 201))
        dailyCaloriesLayout = QVBoxLayout(dailyCaloriesLayoutWidget)
        dailyCaloriesLayout.setContentsMargins(0, 0, 0, 0)
        barDiagramLayout = QVBoxLayout()
        barDiagramInfoLabel = QLabel(dailyCaloriesLayoutWidget, text="Daily consumed calories amount since last reset:")
        barDiagramLayout.addWidget(barDiagramInfoLabel)
        barFoodDiagramChartView = QChartView(dailyCaloriesLayoutWidget)
        barDiagramLayout.addWidget(barFoodDiagramChartView)
        dailyCaloriesLayout.addLayout(barDiagramLayout)
        
        return dailyCaloriesLayout, dailyCaloriesLayoutWidget, barFoodDiagramChartView
    
    
    def createPushButton(self, dimensions, text):
        button = QPushButton(self.centralwidget, text=text)
        button.setGeometry(dimensions)
        return button
    
    def statusBarSetting(self):
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)



#activities about GUI functionality

    def deactivateAtStart(self):
        self.foodListLayoutWidget.setVisible(False)
        self.bmrLayoutWidget.setVisible(False)
        self.sportActivityButton.setVisible(False)
        self.resetFoodButton.setVisible(False)
        self.dailyCaloriesLayoutWidget.setVisible(False)

    
        
    def loadUserDataFromWidgets(self):
        try:
            self.sexData = self.sexComboBoxWidget.currentText().lower()
            self.heightData = int(self.heightWidget.text())
            self.weightData = int(self.weightWidget.text())
            self.age = int(self.ageWidget.text())
            self.enteredFood = self.foodWidget.text()
            self.foodAmount = int(self.foodAmountWidget.text())
            return True
            
        except ValueError:
            self.createAndPrintMessageBox("Incorrect number", "Please enter numbers in lines: height, weight, age, Food amount")
            self.deactivateAtStart()
        
        
    def loadFoodTypesAndSearch(self):
        try:   
            self.foodListWidget.clear()
            if self.loadUserDataFromWidgets():
                self.matchingFoods = findFoodNamesByString(self.caloriesList, self.enteredFood)
                for item in self.matchingFoods:
                    self.foodListWidget.addItem(str(item))
                    
                self.foodListWidget.itemClicked.connect(self.activateBmrAndDiagrams)
                self.foodListLayoutWidget.setVisible(True)
                
        except FileNotFoundError:
            self.createAndPrintMessageBox("Lack of file", "There isn't a calories.csv file in a directory")
        except AttributeError:
            pass

        
    def countBmrFunctions(self, item):
        row = item.text()
        caloriesPer100gFromRow = takeFirstNumberFromString(row)
        foodName = getFoodNameFromRow(row)
        self.bmr = countBMR(self.sexData, self.weightData, self.heightData, self.age)
        self.caloriesAmount = countCaloriesInFoodAmount(self.foodAmount, caloriesPer100gFromRow)
        percentInBmr = percentCaloriesInBMR(self.caloriesAmount, self.bmr)
        
        if foodName in self.todayDifferentFoodsDict.keys():
            self.todayDifferentFoodsDict[foodName] += self.caloriesAmount
        else:
            self.todayDifferentFoodsDict.update({foodName: self.caloriesAmount})
        
        #accomodate calories amount to today's amount
        self.todayCaloriesAmount += self.caloriesAmount
           
        #save numbers to labels
        self.countBmrFunctionLabel.setText(self.formatFLoatToTwoDecimalPoints(self.bmr))
        self.countAmountCaloriesLabel.setText(self.formatFLoatToTwoDecimalPoints(self.caloriesAmount))
        self.percentBmrFunctionLabel.setText(self.formatFLoatToTwoDecimalPoints(percentInBmr))
        

    def activateBmrAndDiagrams(self, item):
        self.countBmrFunctions(item)
        self.createPieChart()
        self.bmrLayoutWidget.setVisible(True)
        self.createBarDiagram()
        self.dailyCaloriesLayoutWidget.setVisible(True)
        self.resetFoodButton.clicked.connect(self.startResetFoods)
        self.resetFoodButton.setVisible(True)
        self.sportActivityButton.clicked.connect(self.sportActivitiesActivate)
        self.sportActivityButton.setVisible(True)
        
        
    def createPieChart(self):
        
        #taking calories amounts and food names from dictionary
        caloriesAmounts = [percentCaloriesInBMR(amount, self.bmr) for amount in self.todayDifferentFoodsDict.values()]
        foodNames = list(self.todayDifferentFoodsDict.keys())
        
        #check if the eaten food exceeds 100%
        #if not, it will be showed in a pie chart
        sumCalories = sum(caloriesAmounts)
        if sumCalories < 100:
            unEatenPercent = 100 - sumCalories
            caloriesAmounts.append(unEatenPercent)
            foodNames.append('Not eaten')
        
        pieChartSeries = QPieSeries(self.circleDiagramChartView)
        
        for food,calories in zip(foodNames,caloriesAmounts):
            pieChartSeries.append(food, calories)
            
        pieChart = QChart()
        pieChart.addSeries(pieChartSeries)
        pieChart.setTitle("Calories amounts in every food eaten today")
        pieChartView = QChartView(pieChart)
        pieChartView.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.circleDiagramChartView.setChart(pieChart)
    
    def createBarDiagram(self):
        
         #loading data from JSON file
        dailyCaloriesAmount = loadDailyCaloriesFromFile()
        
        #plot a diagram only if file exists and is not empty
        if dailyCaloriesAmount is not None:
            dailyCaloriesAmount[str(datetime.now().date())] = self.todayCaloriesAmount
            arguments = list(dailyCaloriesAmount.keys())
            values = list(dailyCaloriesAmount.values())
            
            barSeries = QBarSeries()
            barSet = QBarSet("Dates")
            barSet.append(values)
            barSeries.append(barSet)
            
            #create main view
            barChart = QChart()
            barChart.setAnimationOptions(QChart.NoAnimation)
            barChart.setDropShadowEnabled(False)
            barChart.addSeries(barSeries)
            barChart.setTitle("Daily calories amounts" )
            
            #creation of x axis
            if self.xAxisAttached == False:
                xScale = QBarCategoryAxis()
                xScale.append(arguments)
                barChart.setAxisX(xScale, barSeries)
                barSeries.attachAxis(xScale)
                self.xAxisAttached = True
            
            #creation of y axis with the scale(from 0 to max among calories amounts)
            yScale = QValueAxis()
            yScale.setMin(0)
            yScale.setMax(max(values) * 1.2) 
            yScale.setTickCount(5) 
            barChart.setAxisY(yScale)
            self.yAxisAttached = True
            
            #create a dashed line on the height of BMR value
            dashedLineSeries = QLineSeries()
            dashedLineSeries.append(0, self.bmr)
            dashedLineSeries.append(len(values) - 1, self.bmr)
            pen = QPen(Qt.PenStyle.DashLine)
            dashedLineSeries.setPen(pen)
            barChart.addSeries(dashedLineSeries)
            dashedLineSeries.attachAxis(yScale)
            dashedLineSeries.setName("BMR value")
            
            #create a 'layout' for main view
            barChartView = QChartView(barChart)
            barChartView.setRenderHint(QPainter.RenderHint.Antialiasing)
            self.barFoodDiagramChartView.setChart(barChart)
            
            
    def formatFLoatToTwoDecimalPoints(self, float):
        return f"{float:.2f}"        
    
    
    #message box with template Yes/No
    def createMessageBoxYesNo(self, windowTitle, text):
        question = QMessageBox(self)
        question.setWindowTitle(windowTitle)
        question.setText(text)
        question.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        question.setIcon(QMessageBox.Icon.Question)
        chosenOption = question.exec()
        return chosenOption
            
            
    def startResetFoods(self):
        #check if the flag is false(to avoid multiple appears message box)
        if not self.resetFoodsShows:
            self.resetFoodsShows = True
            QTimer.singleShot(0, self.resetTodayData)        
    
    
    #the process of asking the user about deleting today data
    def resetTodayData(self):
        chosenOption = self.createMessageBoxYesNo("Delete today data?", "Do you want to delete all today's data?")
        if chosenOption == QMessageBox.StandardButton.Yes:
            self.resetToday()
            QTimer.singleShot(0, self.resetPreviousData)   
        else:
            pass
        
        #now reset message boxes can appear
        self.resetFoodsShows = False
        
        
    #delete data from previous days(dailyCalories.json)
    def resetPreviousData(self):
        chosenOption = self.createMessageBoxYesNo("Delete previous data?", "Do you want to delete data from previous days?")        
        if chosenOption == QMessageBox.StandardButton.Yes:
            clearJsonDailyCalories()
        pass
        
    
    def resetUserData(self):
        self.todayCaloriesAmount = 0
        self.todayDifferentFoodsDict = dict()
        self.sexData = None
        self.heightData = 0
        self.weightData = 0
        self.age = 0
        self.enteredFood = ""
        self.foodAmount = 0
        self.bmr = 0

    def resetToday(self):
        self.resetUserData()
        clearJsonTodayEatings()
        self.deactivateAtStart()
        
        
        
        
#creations of activities related layouts
    def createSportActivityLayout(self):
        activityLayoutWidget = QWidget(self.centralwidget)
        activityLayoutWidget.setGeometry(QRect(940, 10, 481, 34))
        activityLayout = QHBoxLayout(activityLayoutWidget)
        sportActivityLabel = QLabel(activityLayoutWidget, text="Sport activity: ")
        activityLayout.addWidget(sportActivityLabel)
        sportActivityWidget = QLineEdit(activityLayoutWidget)
        activityLayout.addWidget(sportActivityWidget)
        return activityLayout, activityLayoutWidget, sportActivityWidget    


    def createActivityListLayout(self):
        listActivitiesLayoutWidget = QWidget(self.centralwidget)
        listActivitiesLayoutWidget.setGeometry(QRect(940, 100, 481, 231))
        listActivitiesLayout = QVBoxLayout(listActivitiesLayoutWidget)
        chooseActivityLabel = QLabel(listActivitiesLayoutWidget, text="Choose type of sport activity: ")
        listActivitiesLayout.addWidget(chooseActivityLabel)
        columnsNameActivitiesLabel = QLabel(listActivitiesLayoutWidget, text="Full name, Calories to burn per kg")
        listActivitiesLayout.addWidget(columnsNameActivitiesLabel)
        sportActivityListWidget = QListWidget(listActivitiesLayoutWidget)
        listActivitiesLayout.addWidget(sportActivityListWidget)
        return listActivitiesLayout, listActivitiesLayoutWidget, sportActivityListWidget
    
    
    def createSpeedLayout(self):
        speedLayoutWidget = QWidget(self.centralwidget)
        speedLayoutWidget.setGeometry(QRect(940, 340, 481, 191))
        speedLabelsLayout = QVBoxLayout(speedLayoutWidget)
        averageSpeedLabel = QLabel(speedLayoutWidget, text="Average speed during activity:")
        speedLabelsLayout.addWidget(averageSpeedLabel)
        currentSpeedLayout = QHBoxLayout()
        currentSpeedLabel = QLabel(speedLayoutWidget)
        currentSpeedLayout.addWidget(currentSpeedLabel)
        speedUnitLabel = QLabel(speedLayoutWidget, text="km/h")
        currentSpeedLayout.addWidget(speedUnitLabel)
        speedLabelsLayout.addLayout(currentSpeedLayout)
        speedSliderWidget = QSlider(Qt.Horizontal)
        speedLayoutWidget.setLayout(speedLabelsLayout)
        speedLabelsLayout.addWidget(speedSliderWidget)
        return speedLabelsLayout, speedLayoutWidget, currentSpeedLabel, speedSliderWidget
    
    
    def createEstimatingTimeLayout(self):
        estimatingTimeLayoutWidget = QWidget(self.centralwidget)
        estimatingTimeLayoutWidget.setGeometry(QRect(950, 560, 241, 91))
        estimatingTimeLayout = QVBoxLayout(estimatingTimeLayoutWidget)
        estimatingTimeLabel = QLabel(estimatingTimeLayoutWidget, text="Estimating time to burn today's calories:")
        estimatingTimeLayout.addWidget(estimatingTimeLabel)
        countedTimeLabel = QLabel(estimatingTimeLayoutWidget)
        estimatingTimeLayout.addWidget(countedTimeLabel)
        return estimatingTimeLayout, estimatingTimeLayoutWidget, countedTimeLabel
        
  
    def createAllActivityRelatedLayouts(self):
        self.activityLayout, self.activityLayoutWidget, self.sportActivityWidget = self.createSportActivityLayout()
        self.confirmActivity = self.createPushButton(QRect(1150, 50, 131, 24), text="Confirm sport activity")
        self.listActivitiesLayout, self.listActivitiesLayoutWidget, self.sportActivityListWidget = self.createActivityListLayout()
        self.speedLayout, self.speedLayoutWidget, self.currentSpeedLabel, self.speedSliderWidget = self.createSpeedLayout()
        self.estimatingTimeLayout, self.estimatingTimeLayoutWidget, self.countedTimeLabel = self.createEstimatingTimeLayout()
        self.resetActivitiesButton = self.createPushButton(QRect(1280, 610, 131, 41), text="Reset sport activities")
    
    
    #first step of creating activities related GUI part
    def sportActivitiesActivate(self):
        #read activities types from a file 
        try:
            self.activitiesDict = loadActivitiesData()
            #now are creating all activity related layouts
            self.createAllActivityRelatedLayouts()
            self.activityLayoutWidget.setVisible(True)
            self.confirmActivity.clicked.connect(self.printActivities)
            self.confirmActivity.setVisible(True)
            self.deactivateActivityLayoutsAtStart()
        except FileNotFoundError:
            self.createAndPrintMessageBox("Activities file not found", "File with activities not found ")
            pass
        
        
    def printActivities(self):
        self.sportActivityListWidget.clear()
        self.enteredActivity = self.sportActivityWidget.text()
        self.matchingActivities = findActivitiesByString(self.activitiesDict, self.enteredActivity)
        for activity in self.matchingActivities.items():
            self.sportActivityListWidget.addItem(str(activity))
            
        self.sportActivityListWidget.itemClicked.connect(self.countSpeed)
        self.listActivitiesLayoutWidget.setVisible(True)

        #the flag to avoid multiple appears of message box
        self.resetActivitiesShows = False

    def countSpeed(self, activity):
        #check if the value is list or float(if a speed is a crucial factor to burn calories)
        valueString = correctValueFromString(activity.text())
        typeValue = listOrFloat(valueString)

        try:
            if typeValue == 'list':
                self.speedLayoutWidget.setVisible(True)
                self.listSpeeds = ast.literal_eval(valueString)
                self.minimumSpeed = getMinSpeedEnteredByUser(self.listSpeeds)
                self.speedSliderWidget.setMinimum(self.minimumSpeed)
                self.speedSliderWidget.setMaximum(getMaxSpeedInList(self.listSpeeds))
                self.speedSliderWidget.setTickPosition(QSlider.TickPosition.TicksBelow)
                self.speedSliderWidget.setTickInterval(2)
                self.currentSpeedLabel.setText(str(self.minimumSpeed))
                self.speedSliderWidget.valueChanged.connect(self.sliderChanged)
            else:
                self.speedLayoutWidget.setVisible(False)
                self.estimatingTime = getEstimatingTimeSlope(float(valueString), self.weightData, self.caloriesAmount)
                self.countedTimeLabel.setText(f"Hours: {self.estimatingTime[0]}, minutes: {self.estimatingTime[1]}")
                self.estimatingTimeLayoutWidget.setVisible(True)
                self.resetActivitiesButton.clicked.connect(self.resetActivities)
                self.resetActivitiesButton.setVisible(True)
        except ZeroDivisionError:
            self.createAndPrintMessageBox("No user data", "Please enter user data before looking for sport activites")
            self.activityLayoutWidget.setVisible(False)
            self.confirmActivity.setVisible(False)
            self.deactivateActivityLayoutsAtStart()


    def sliderChanged(self):
        try:
            self.currentSpeed = self.sender().value()
            self.currentSpeedLabel.setText(self.formatFLoatToTwoDecimalPoints(self.currentSpeed))
            slopeFunction = getSlopeFromCorrectSpeedInterval(self.listSpeeds, self.currentSpeed)
            self.estimatingTime = getEstimatingTimeSlope(slopeFunction, self.weightData, self.caloriesAmount)
            self.countedTimeLabel.setText(f"Hours: {self.estimatingTime[0]}, minutes: {self.estimatingTime[1]}")
            self.estimatingTimeLayoutWidget.setVisible(True)
            self.resetActivitiesButton.clicked.connect(self.startResetActivities)
            self.resetActivitiesButton.setVisible(True)
        except ZeroDivisionError:
            self.createAndPrintMessageBox("No user data", "Please enter user data before looking for sport activites")
            self.activityLayoutWidget.setVisible(False)
            self.confirmActivity.setVisible(False)
            self.deactivateActivityLayoutsAtStart()
        
        
    def startResetActivities(self):
        if not self.resetActivitiesShows:
            self.resetActivitiesShows = True
            QTimer.singleShot(0, self.resetActivities)
        
    
    def deactivateActivityLayoutsAtStart(self):
        self.listActivitiesLayoutWidget.setVisible(False)
        self.speedLayoutWidget.setVisible(False)
        self.estimatingTimeLayoutWidget.setVisible(False)
        self.resetActivitiesButton.setVisible(False)
    
    
    def resetActivitiesData(self):
        self.currentSpeed = 0
        self.listSpeeds = []
        self.estimatingTime = None
        self.deactivateActivityLayoutsAtStart()
    
    
    def resetActivities(self):
        chosenOption = self.createMessageBoxYesNo("Delete activities?", "Do you want to delete all activities data?")
        if chosenOption == QMessageBox.StandardButton.Yes:
            self.resetActivitiesData()
            self.sportActivitiesActivate()
        pass
        
        
    def closeEvent(self, event):
        #print a question only if calories amount today is not zero
        if self.todayCaloriesAmount > 0:
            chosenOption = self.createMessageBoxYesNo("Save today calories?", "Would you like to save today's calories amount to a file?")

            if chosenOption == QMessageBox.StandardButton.Yes:
                event.accept()
                saveTodayCaloriesToFile(self.todayCaloriesAmount)
                saveTodayEatings(self.todayDifferentFoodsDict)
            elif chosenOption == QMessageBox.StandardButton.No:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()
        
        
    #template with OK(info only) message box
    def createAndPrintMessageBox(self, windowTitle, text):
        msgBox = QMessageBox()
        msgBox.setWindowTitle(windowTitle)
        msgBox.setText(text)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()


app = QApplication(sys.argv)
window = FoodMainWindow()
window.show()
sys.exit(app.exec())
