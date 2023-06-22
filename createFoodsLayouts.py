from PySide6.QtCore import QRect
from PySide6.QtWidgets import (QHBoxLayout,QLabel, QLineEdit, 
                               QListWidget,QVBoxLayout, QWidget)
from PySide6.QtCharts import QChartView


#layout type with horizontal layout inside vertical layout
def userDataWithUnitLayoutFL(centralwidget, dimensions, dataTypeName, unitName):
    layoutWidget = QWidget(centralwidget)
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
def userDataWithoutUnitFL(dataTypeName, dataWidget, layoutWidget):
    layout = QVBoxLayout(layoutWidget)
    layout.setContentsMargins(0, 0, 0, 0)
    label = QLabel(layoutWidget, text=dataTypeName)
    layout.addWidget(label)
    layout.addWidget(dataWidget)
    return layout
    
    
def createFoodListLayoutFL(centralwidget):
        foodListLayoutWidget = QWidget(centralwidget)
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
    
    
def createBmrInfoLayoutFL(centralwidget):
        bmrLayoutWidget = QWidget(centralwidget)
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
            
            
def createDailyCaloriesFL(centralwidget):
        dailyCaloriesLayoutWidget = QWidget(centralwidget)
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