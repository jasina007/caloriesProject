import ast
from PySide6.QtCore import (QRect, QTimer, Qt)

from PySide6.QtWidgets import (QHBoxLayout,QLabel, QLineEdit, 
                               QListWidget, QVBoxLayout, QWidget, QMessageBox, QSlider)
from loadActivities import loadActivitiesData
from functionsAndDiagrams import (saveTodayEatings, findActivitiesByString, correctValueFromString,
                                  listOrFloat, getMinSpeedEnteredByUser, getSlopeFromCorrectSpeedInterval,
                                  getEstimatingTimeSlope, getMaxSpeedInList)



#creations of activities related layouts
def createSportActivityLayoutAF(centralwidget):
    activityLayoutWidget = QWidget(centralwidget)
    activityLayoutWidget.setGeometry(QRect(940, 10, 481, 34))
    activityLayout = QHBoxLayout(activityLayoutWidget)
    sportActivityLabel = QLabel(activityLayoutWidget, text="Sport activity: ")
    activityLayout.addWidget(sportActivityLabel)
    sportActivityWidget = QLineEdit(activityLayoutWidget)
    activityLayout.addWidget(sportActivityWidget)
    return activityLayout, activityLayoutWidget, sportActivityWidget    


def createActivityListLayoutAF(centralwidget):
    listActivitiesLayoutWidget = QWidget(centralwidget)
    listActivitiesLayoutWidget.setGeometry(QRect(940, 100, 481, 231))
    listActivitiesLayout = QVBoxLayout(listActivitiesLayoutWidget)
    chooseActivityLabel = QLabel(listActivitiesLayoutWidget, text="Choose type of sport activity: ")
    listActivitiesLayout.addWidget(chooseActivityLabel)
    columnsNameActivitiesLabel = QLabel(listActivitiesLayoutWidget, text="Full name, Calories to burn per kg")
    listActivitiesLayout.addWidget(columnsNameActivitiesLabel)
    sportActivityListWidget = QListWidget(listActivitiesLayoutWidget)
    listActivitiesLayout.addWidget(sportActivityListWidget)
    return listActivitiesLayout, listActivitiesLayoutWidget, sportActivityListWidget


def createSpeedLayoutAF(centralwidget):
    speedLayoutWidget = QWidget(centralwidget)
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


def createEstimatingTimeLayoutAF(centralwidget):
    estimatingTimeLayoutWidget = QWidget(centralwidget)
    estimatingTimeLayoutWidget.setGeometry(QRect(950, 560, 241, 91))
    estimatingTimeLayout = QVBoxLayout(estimatingTimeLayoutWidget)
    estimatingTimeLabel = QLabel(estimatingTimeLayoutWidget, text="Estimating time to burn today's calories:")
    estimatingTimeLayout.addWidget(estimatingTimeLabel)
    countedTimeLabel = QLabel(estimatingTimeLayoutWidget)
    estimatingTimeLayout.addWidget(countedTimeLabel)
    return estimatingTimeLayout, estimatingTimeLayoutWidget, countedTimeLabel
    

def createAllActivityRelatedLayoutsAF(self):
    self.activityLayout, self.activityLayoutWidget, self.sportActivityWidget = self.createSportActivityLayout()
    self.confirmActivity = self.createPushButton(QRect(1150, 50, 131, 24), text="Confirm sport activity")
    self.listActivitiesLayout, self.listActivitiesLayoutWidget, self.sportActivityListWidget = self.createActivityListLayout()
    self.speedLayout, self.speedLayoutWidget, self.currentSpeedLabel, self.speedSliderWidget = self.createSpeedLayout()
    self.estimatingTimeLayout, self.estimatingTimeLayoutWidget, self.countedTimeLabel = self.createEstimatingTimeLayout()
    self.resetActivitiesButton = self.createPushButton(QRect(1280, 610, 131, 41), text="Reset sport activities")


#first step of creating activities related GUI part
def sportActivitiesActivateAF(self):
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
    
    
def printActivitiesAF(self):
    self.sportActivityListWidget.clear()
    self.enteredActivity = self.sportActivityWidget.text()
    self.matchingActivities = findActivitiesByString(self.activitiesDict, self.enteredActivity)
    for activity in self.matchingActivities.items():
        self.sportActivityListWidget.addItem(str(activity))
        
    self.sportActivityListWidget.itemClicked.connect(self.countSpeed)
    self.listActivitiesLayoutWidget.setVisible(True)

    #the flag to avoid multiple appears of message box
    self.resetActivitiesShows = False


#method to avoid repeating code
def countAndPrintEstimatingTimeAF(self, slope):
    self.estimatingTime = getEstimatingTimeSlope(slope, self.weightData, self.caloriesAmount)
    self.countedTimeLabel.setText(f"Hours: {self.estimatingTime[0]}, minutes: {self.estimatingTime[1]}")
    self.estimatingTimeLayoutWidget.setVisible(True)
    self.resetActivitiesButton.clicked.connect(self.startResetActivities)
    self.resetActivitiesButton.setVisible(True)


#method which count all need to define estimating time 
def countSpeedAF(self, activity):
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
            self.currentSpeedLabel.setText(self.formatFLoatToTwoDecimalPoints(self.minimumSpeed))
            self.speedSliderWidget.valueChanged.connect(self.sliderChanged)
        else:
            self.speedLayoutWidget.setVisible(False)
            self.countAndPrintEstimatingTime(float(valueString))
            
    #dividing by zero is due to a lack of user data
    except ZeroDivisionError:
        self.createAndPrintMessageBox("No user data", "Please enter user data before looking for sport activites")
        self.activityLayoutWidget.setVisible(False)
        self.confirmActivity.setVisible(False)
        self.deactivateActivityLayoutsAtStart()


def sliderChangedAF(self):
    try:
        self.currentSpeed = self.sender().value()
        self.currentSpeedLabel.setText(self.formatFLoatToTwoDecimalPoints(self.currentSpeed))
        slopeFunction = getSlopeFromCorrectSpeedInterval(self.listSpeeds, self.currentSpeed)
        self.countAndPrintEstimatingTime(slopeFunction)
    except ZeroDivisionError:
        self.createAndPrintMessageBox("No user data", "Please enter user data before looking for sport activites")
        self.activityLayoutWidget.setVisible(False)
        self.confirmActivity.setVisible(False)
        self.deactivateActivityLayoutsAtStart()
    
    
def startResetActivitiesAF(self):
    if not self.resetActivitiesShows:
        self.resetActivitiesShows = True
        QTimer.singleShot(0, self.resetActivities)
    

def deactivateActivityLayoutsAtStartAF(self):
    self.listActivitiesLayoutWidget.setVisible(False)
    self.speedLayoutWidget.setVisible(False)
    self.estimatingTimeLayoutWidget.setVisible(False)
    self.resetActivitiesButton.setVisible(False)


def resetActivitiesDataAF(self):
    self.currentSpeed = 0
    self.listSpeeds = []
    self.estimatingTime = None
    self.deactivateActivityLayoutsAtStart()


def resetActivitiesAF(self):
    chosenOption = self.createMessageBoxYesNo("Delete activities?", "Do you want to delete all activities data?")
    if chosenOption == QMessageBox.StandardButton.Yes:
        self.resetActivitiesData()
        self.sportActivitiesActivate()
    pass
    
    
def closeEventAF(self, event):
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
def createAndPrintMessageBoxAF(windowTitle, text):
    msgBox = QMessageBox()
    msgBox.setWindowTitle(windowTitle)
    msgBox.setText(text)
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()
