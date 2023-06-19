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
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QRect(33, 20, 71, 51))
        
        #sex layout
        self.sexLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.sexLayout.setContentsMargins(0, 0, 0, 0)
        self.sexLabel = QLabel(self.verticalLayoutWidget, text="Sex")
        self.sexLayout.addWidget(self.sexLabel)
        self.sexComboBoxWidget = QComboBox(self.verticalLayoutWidget)
        self.sexComboBoxWidget.addItem("Female")
        self.sexComboBoxWidget.addItem("Male")
        self.sexLayout.addWidget(self.sexComboBoxWidget)

        #height layout
        self.heightLayoutWidget = QWidget(self.centralwidget)
        self.heightLayoutWidget.setGeometry(QRect(113, 20, 80, 51))
        self.heightLayout = QVBoxLayout(self.heightLayoutWidget)
        self.heightLayout.setContentsMargins(0, 0, 0, 0)
        self.heightLabel = QLabel(self.heightLayoutWidget, text="Height")
        self.heightLayout.addWidget(self.heightLabel)
        self.heightHorizontalLayout = QHBoxLayout()
        self.heightWidget = QLineEdit(self.heightLayoutWidget)
        self.heightHorizontalLayout.addWidget(self.heightWidget)
        self.cmLabel = QLabel(self.heightLayoutWidget, text="cm")
        self.heightHorizontalLayout.addWidget(self.cmLabel)
        self.heightLayout.addLayout(self.heightHorizontalLayout)

        #weight layout
        self.weightLayoutWidget = QWidget(self.centralwidget)
        self.weightLayoutWidget.setGeometry(QRect(194, 20, 78, 51))
        self.weightLayout = QVBoxLayout(self.weightLayoutWidget)
        self.weightLayout.setContentsMargins(0, 0, 0, 0)
        self.weightLabel = QLabel(self.weightLayoutWidget, text="Weight")
        self.weightLayout.addWidget(self.weightLabel)
        self.weightHorizontalLayout = QHBoxLayout()
        self.weightWidget = QLineEdit(self.weightLayoutWidget)
        self.weightHorizontalLayout.addWidget(self.weightWidget)
        self.kgLabel = QLabel(self.weightLayoutWidget, text="kg")
        self.weightHorizontalLayout.addWidget(self.kgLabel)
        self.weightLayout.addLayout(self.weightHorizontalLayout)

        #age layout
        self.ageLayoutWidget = QWidget(self.centralwidget)
        self.ageLayoutWidget.setGeometry(QRect(274, 20, 112, 51))
        self.ageLayout = QVBoxLayout(self.ageLayoutWidget)
        self.ageLayout.setContentsMargins(0, 0, 0, 0)
        self.ageLabel = QLabel(self.ageLayoutWidget, text="Age")
        self.ageLayout.addWidget(self.ageLabel)
        self.ageHorizontalLayout = QHBoxLayout()
        self.ageWidget = QLineEdit(self.ageLayoutWidget)
        self.ageHorizontalLayout.addWidget(self.ageWidget)
        self.yearOldLabel = QLabel(self.ageLayoutWidget, text="years old")
        self.ageHorizontalLayout.addWidget(self.yearOldLabel)
        self.ageLayout.addLayout(self.ageHorizontalLayout)

        #food layout
        self.foodLayoutWidget = QWidget(self.centralwidget)
        self.foodLayoutWidget.setGeometry(QRect(392, 20, 151, 51))
        self.foodLayout = QVBoxLayout(self.foodLayoutWidget)
        self.foodLayout.setContentsMargins(0, 0, 0, 0)
        self.foodLabel = QLabel(self.foodLayoutWidget, text="Food")
        self.foodLayout.addWidget(self.foodLabel)
        self.foodWidget = QLineEdit(self.foodLayoutWidget)
        self.foodLayout.addWidget(self.foodWidget)

        #food amount layout
        self.foodAmountLayoutWidget = QWidget(self.centralwidget)
        self.foodAmountLayoutWidget.setGeometry(QRect(553, 20, 91, 51))
        self.foodAmountLayout = QVBoxLayout(self.foodAmountLayoutWidget)
        self.foodAmountLayout.setContentsMargins(0, 0, 0, 0)
        self.foodAmountLabel = QLabel(self.foodAmountLayoutWidget, text="Food amount")
        self.foodAmountLayout.addWidget(self.foodAmountLabel)
        self.foodAmountHorizontalLayout = QHBoxLayout()
        self.foodAmountWidget = QLineEdit(self.foodAmountLayoutWidget)
        self.foodAmountHorizontalLayout.addWidget(self.foodAmountWidget)
        self.unitFoodLabel = QLabel(self.foodAmountLayoutWidget, text="g/ml")
        self.foodAmountHorizontalLayout.addWidget(self.unitFoodLabel)
        self.foodAmountLayout.addLayout(self.foodAmountHorizontalLayout)


        self.confirmDataButton = QPushButton(self.centralwidget, text="Confirm data")
        self.confirmDataButton.setGeometry(QRect(150, 80, 91, 24))
        
        #food list layout
        self.foodListLayoutWidget = QWidget(self.centralwidget)
        self.foodListLayoutWidget.setGeometry(QRect(20, 120, 326, 251))
        self.foodListLayout = QVBoxLayout(self.foodListLayoutWidget)
        self.foodListLayout.setContentsMargins(0, 0, 0, 0)
        self.chooseFoodLabel = QLabel(self.foodListLayoutWidget, text="Choose kind of 'Food' (entered above):")
        self.foodListLayout.addWidget(self.chooseFoodLabel)
        self.columnsFoodLabel = QLabel(self.foodListLayoutWidget, text="Full name, Type, Calories per 100g/ml, Kilojoules per 100g/ml")
        self.foodListLayout.addWidget(self.columnsFoodLabel)
        self.foodListWidget = QListWidget(self.foodListLayoutWidget)
        self.foodListLayout.addWidget(self.foodListWidget)


        self.bmrLayoutWidget = QWidget(self.centralwidget)
        self.bmrLayoutWidget.setGeometry(QRect(360, 90, 301, 281))
        self.bmrLayout = QVBoxLayout(self.bmrLayoutWidget)
        self.bmrLayout.setContentsMargins(0, 0, 0, 0)
        self.caloriesInfoLayout = QVBoxLayout()
        self.bmrHorizontalLayout = QHBoxLayout()
        self.bmrLabel = QLabel(self.bmrLayoutWidget, text="Basal Metabolic Rate")
        self.bmrHorizontalLayout.addWidget(self.bmrLabel)
        self.countBmrFunctionLabel = QLabel(self.bmrLayoutWidget)
        self.bmrHorizontalLayout.addWidget(self.countBmrFunctionLabel)
        self.calLabel = QLabel(self.bmrLayoutWidget, text="cal")
        self.bmrHorizontalLayout.addWidget(self.calLabel)
        self.caloriesInfoLayout.addLayout(self.bmrHorizontalLayout)
        self.foodCaloriesHorizontalLayout = QHBoxLayout()
        self.caloriesInfoLabel = QLabel(self.bmrLayoutWidget, text="Calories in chosen food in entered amount: ")
        self.foodCaloriesHorizontalLayout.addWidget(self.caloriesInfoLabel)
        self.countAmountCaloriesLabel = QLabel(self.bmrLayoutWidget)
        self.foodCaloriesHorizontalLayout.addWidget(self.countAmountCaloriesLabel)
        self.calLabel_2 = QLabel(self.bmrLayoutWidget, text="cal")
        self.foodCaloriesHorizontalLayout.addWidget(self.calLabel_2)
        self.caloriesInfoLayout.addLayout(self.foodCaloriesHorizontalLayout)
        self.percentHorizontalLayout = QHBoxLayout()
        self.bmrInfoLabel = QLabel(self.bmrLayoutWidget, text="Percentage amount of food calories in BMR: ")
        self.percentHorizontalLayout.addWidget(self.bmrInfoLabel)
        self.percentBmrFunctionLabel = QLabel(self.bmrLayoutWidget)
        self.percentHorizontalLayout.addWidget(self.percentBmrFunctionLabel)
        self.percentSignLabel = QLabel(self.bmrLayoutWidget, text="%")
        self.percentHorizontalLayout.addWidget(self.percentSignLabel)
        self.caloriesInfoLayout.addLayout(self.percentHorizontalLayout)
        self.circleDiagramInfoLabel = QLabel(self.bmrLayoutWidget, text="Circle diagram with all entered food types:")
        self.caloriesInfoLayout.addWidget(self.circleDiagramInfoLabel)
        self.circleDiagramWidget = QGraphicsView(self.bmrLayoutWidget)
        self.caloriesInfoLayout.addWidget(self.circleDiagramWidget)
        self.bmrLayout.addLayout(self.caloriesInfoLayout)

        #bottom buttons
        self.sportActivityButton = QPushButton(self.centralwidget, text="Sport activity")
        self.sportActivityButton.setGeometry(QRect(550, 610, 101, 41))
        self.resetFoodButton = QPushButton(self.centralwidget, text="Reset foods")
        self.resetFoodButton.setGeometry(QRect(30, 610, 111, 41))
        
        #daily calories layout
        self.dailyCaloriesLayoutWidget = QWidget(self.centralwidget)
        self.dailyCaloriesLayoutWidget.setGeometry(QRect(20, 390, 641, 211))
        self.dailyCaloriesLayout = QVBoxLayout(self.dailyCaloriesLayoutWidget)
        self.dailyCaloriesLayout.setContentsMargins(0, 0, 0, 0)
        self.barDiagramLayout = QVBoxLayout()
        self.barDiagramInfoLabel = QLabel(self.dailyCaloriesLayoutWidget, text="Daily consumed calories amount since last reset:")
        self.barDiagramLayout.addWidget(self.barDiagramInfoLabel)
        self.barFoodDiagramWidget = QGraphicsView(self.dailyCaloriesLayoutWidget)
        self.barDiagramLayout.addWidget(self.barFoodDiagramWidget)
        self.dailyCaloriesLayout.addLayout(self.barDiagramLayout)
        
        #set status bar and central widget
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar()
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

    
app = QApplication(sys.argv)
window = FoodMainWindow()
window.show()
sys.exit(app.exec())