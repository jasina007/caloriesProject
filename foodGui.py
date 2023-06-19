from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)
import sys

class FoodMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(680, 677)
        self.setWindowTitle("Food types window")
        self.centralwidget = QWidget()
        
        #there are 2 data layouts types: with vertical layout only and with horizontal layout inside a vertical layout
        #sex layout
        self.sexLayoutWidget = QWidget(self.centralwidget)
        self.sexLayoutWidget.setGeometry(QRect(33, 20, 71, 51))
        self.sexComboBoxWidget = QComboBox(self.sexLayoutWidget)
        self.sexComboBoxWidget.addItem("Female")
        self.sexComboBoxWidget.addItem("Male")
        self.sexLayout = self.userDataWithoutUnit("Sex", self.sexComboBoxWidget, self.sexLayoutWidget)
        
        #height layout
        self.heightLayout, self.heightLayoutWidget, self.heightWidget = self.userDataWithUnitLayout(QRect(113, 20, 80, 51), "Height", "cm")

        #weight layout
        self.weightLayout, self.weightLayoutWidget, self.weightWidget = self.userDataWithUnitLayout(QRect(194, 20, 78, 51), "Weight", "kg")

        #age layout
        self.ageLayout, self.ageLayoutWidget, self.ageWidget = self.userDataWithUnitLayout(QRect(274, 20, 112, 51), "Age", "years old")

        #food layout
        foodLayoutWidget = QWidget(self.centralwidget)
        foodLayoutWidget.setGeometry(QRect(392, 20, 151, 51))
        self.foodWidget = QLineEdit(foodLayoutWidget)
        self.foodLayout = self.userDataWithoutUnit("Food", self.foodWidget, foodLayoutWidget)

        #food amount layout
        self.foodAmountLayout, self.foodAmountLayoutWidget, self.foodAmountWidget = self.userDataWithUnitLayout(QRect(553, 20, 91, 51), "Food amount", "g/ml")

        #confirm data button
        self.confirmDataButton = self.createPushButton(QRect(150, 80, 91, 24), "Confirm data")
        
        
        #food list layout        
        self.foodListLayout, self.foodListLayoutWidget, self.foodListWidget = self.createFoodListLayout()

        #BMR data layout
        self.bmrLayout, self.bmrLayoutWidget, self.circleDiagramWidget, self.countBmrFunctionLabel, \
            self.countAmountCaloriesLabel, self.percentBmrFunctionLabel = self.createBmrInfoLayout()

        #bottom buttons
        self.sportActivityButton = self.createPushButton(QRect(550, 610, 101, 41), "Sport activity")
        self.resetFoodButton = self.createPushButton(QRect(30, 610, 111, 41), "Reset foods")
    
        #daily calories layout
        self.dailyCaloriesLayout, self.dailyCaloriesLayoutWidget, self.barFoodDiagramWidget = self.createDailyCalories()
        
        #deactivate most layouts at start of the app
        self.deactivateAtStart()
        
        #set status bar and central widget
        self.setCentralWidget(self.centralwidget)
        self.statusBarSetting()


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
        foodListLayoutWidget.setGeometry(QRect(20, 120, 326, 251))
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
        bmrLayoutWidget.setGeometry(QRect(360, 90, 301, 281))
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
        circleDiagramWidget = QGraphicsView(bmrLayoutWidget)
        caloriesInfoLayout.addWidget(circleDiagramWidget)
        bmrLayout.addLayout(caloriesInfoLayout)
        
        return bmrLayout, bmrLayoutWidget, circleDiagramWidget, countBmrFunctionLabel, \
            countAmountCaloriesLabel, percentBmrFunctionLabel
    
    
    def createDailyCalories(self):
        dailyCaloriesLayoutWidget = QWidget(self.centralwidget)
        dailyCaloriesLayoutWidget.setGeometry(QRect(20, 390, 641, 211))
        dailyCaloriesLayout = QVBoxLayout(dailyCaloriesLayoutWidget)
        dailyCaloriesLayout.setContentsMargins(0, 0, 0, 0)
        barDiagramLayout = QVBoxLayout()
        barDiagramInfoLabel = QLabel(dailyCaloriesLayoutWidget, text="Daily consumed calories amount since last reset:")
        barDiagramLayout.addWidget(barDiagramInfoLabel)
        barFoodDiagramWidget = QGraphicsView(dailyCaloriesLayoutWidget)
        barDiagramLayout.addWidget(barFoodDiagramWidget)
        dailyCaloriesLayout.addLayout(barDiagramLayout)
        
        return dailyCaloriesLayout, dailyCaloriesLayoutWidget, barFoodDiagramWidget
        
    
    def createPushButton(self, dimensions, text):
        button = QPushButton(self.centralwidget, text=text)
        button.setGeometry(dimensions)
        return button
    
    def statusBarSetting(self):
        self.statusbar = QStatusBar()
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)


    def deactivateAtStart(self):
        self.foodListLayoutWidget.setVisible(False)
        self.bmrLayoutWidget.setVisible(False)
        self.sportActivityButton.setVisible(False)
        self.resetFoodButton.setVisible(False)
        self.dailyCaloriesLayoutWidget.setVisible(False)


app = QApplication(sys.argv)
window = FoodMainWindow()
window.show()
sys.exit(app.exec())