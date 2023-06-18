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

class ui_MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.resize(669, 665)
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(19, 10, 71, 51))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.sexLabel = QLabel(self.verticalLayoutWidget)
        self.sexLabel.setObjectName(u"sexLabel")

        self.verticalLayout.addWidget(self.sexLabel)

        self.sexComboBoxWidget = QComboBox(self.verticalLayoutWidget)
        self.sexComboBoxWidget.addItem("")
        self.sexComboBoxWidget.addItem("")
        self.sexComboBoxWidget.setObjectName(u"sexComboBoxWidget")

        self.verticalLayout.addWidget(self.sexComboBoxWidget)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(99, 10, 80, 51))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.heightLabel = QLabel(self.verticalLayoutWidget_2)
        self.heightLabel.setObjectName(u"heightLabel")

        self.verticalLayout_2.addWidget(self.heightLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.heightWidget = QLineEdit(self.verticalLayoutWidget_2)
        self.heightWidget.setObjectName(u"heightWidget")

        self.horizontalLayout.addWidget(self.heightWidget)

        self.cmLabel = QLabel(self.verticalLayoutWidget_2)
        self.cmLabel.setObjectName(u"cmLabel")

        self.horizontalLayout.addWidget(self.cmLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(181, 10, 78, 51))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.weightLabel = QLabel(self.verticalLayoutWidget_3)
        self.weightLabel.setObjectName(u"weightLabel")

        self.verticalLayout_3.addWidget(self.weightLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.weightWidget = QLineEdit(self.verticalLayoutWidget_3)
        self.weightWidget.setObjectName(u"weightWidget")

        self.horizontalLayout_2.addWidget(self.weightWidget)

        self.kgLabel = QLabel(self.verticalLayoutWidget_3)
        self.kgLabel.setObjectName(u"kgLabel")

        self.horizontalLayout_2.addWidget(self.kgLabel)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(260, 10, 112, 51))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ageLabel = QLabel(self.verticalLayoutWidget_4)
        self.ageLabel.setObjectName(u"ageLabel")

        self.verticalLayout_4.addWidget(self.ageLabel)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ageWidget = QLineEdit(self.verticalLayoutWidget_4)
        self.ageWidget.setObjectName(u"ageWidget")

        self.horizontalLayout_4.addWidget(self.ageWidget)

        self.yearOldLabel = QLabel(self.verticalLayoutWidget_4)
        self.yearOldLabel.setObjectName(u"yearOldLabel")

        self.horizontalLayout_4.addWidget(self.yearOldLabel)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalLayoutWidget_5 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(378, 10, 151, 51))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.foodLabel = QLabel(self.verticalLayoutWidget_5)
        self.foodLabel.setObjectName(u"foodLabel")

        self.verticalLayout_5.addWidget(self.foodLabel)

        self.foodWidget = QLineEdit(self.verticalLayoutWidget_5)
        self.foodWidget.setObjectName(u"foodWidget")

        self.verticalLayout_5.addWidget(self.foodWidget)

        self.verticalLayoutWidget_6 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(539, 10, 89, 51))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.foodAmountLabel = QLabel(self.verticalLayoutWidget_6)
        self.foodAmountLabel.setObjectName(u"foodAmountLabel")

        self.verticalLayout_6.addWidget(self.foodAmountLabel)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.foodAmountWidget = QLineEdit(self.verticalLayoutWidget_6)
        self.foodAmountWidget.setObjectName(u"foodAmountWidget")

        self.horizontalLayout_3.addWidget(self.foodAmountWidget)

        self.unitFoodLabel = QLabel(self.verticalLayoutWidget_6)
        self.unitFoodLabel.setObjectName(u"unitFoodLabel")

        self.horizontalLayout_3.addWidget(self.unitFoodLabel)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.confirmDataButton = QPushButton(self.centralwidget)
        self.confirmDataButton.setObjectName(u"confirmDataButton")
        self.confirmDataButton.setGeometry(QRect(140, 70, 91, 24))
        self.verticalLayoutWidget_7 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(9, 110, 326, 251))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.chooseFoodLabel = QLabel(self.verticalLayoutWidget_7)
        self.chooseFoodLabel.setObjectName(u"chooseFoodLabel")

        self.verticalLayout_7.addWidget(self.chooseFoodLabel)

        self.columnsFoodLabel = QLabel(self.verticalLayoutWidget_7)
        self.columnsFoodLabel.setObjectName(u"columnsFoodLabel")

        self.verticalLayout_7.addWidget(self.columnsFoodLabel)

        self.foodListWidget = QListWidget(self.verticalLayoutWidget_7)
        self.foodListWidget.setObjectName(u"foodListWidget")

        self.verticalLayout_7.addWidget(self.foodListWidget)

        self.verticalLayoutWidget_8 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(349, 80, 301, 281))
        self.verticalLayout_15 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.bmrLabel = QLabel(self.verticalLayoutWidget_8)
        self.bmrLabel.setObjectName(u"bmrLabel")

        self.horizontalLayout_5.addWidget(self.bmrLabel)

        self.countBmrFunctionLabel = QLabel(self.verticalLayoutWidget_8)
        self.countBmrFunctionLabel.setObjectName(u"countBmrFunctionLabel")

        self.horizontalLayout_5.addWidget(self.countBmrFunctionLabel)

        self.calLabel = QLabel(self.verticalLayoutWidget_8)
        self.calLabel.setObjectName(u"calLabel")

        self.horizontalLayout_5.addWidget(self.calLabel)


        self.verticalLayout_12.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.caloriesInfoLabel = QLabel(self.verticalLayoutWidget_8)
        self.caloriesInfoLabel.setObjectName(u"caloriesInfoLabel")

        self.horizontalLayout_6.addWidget(self.caloriesInfoLabel)

        self.countAmountCaloriesLabel = QLabel(self.verticalLayoutWidget_8)
        self.countAmountCaloriesLabel.setObjectName(u"countAmountCaloriesLabel")

        self.horizontalLayout_6.addWidget(self.countAmountCaloriesLabel)

        self.calLabel_2 = QLabel(self.verticalLayoutWidget_8)
        self.calLabel_2.setObjectName(u"calLabel_2")

        self.horizontalLayout_6.addWidget(self.calLabel_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.bmrInfoLabel = QLabel(self.verticalLayoutWidget_8)
        self.bmrInfoLabel.setObjectName(u"bmrInfoLabel")

        self.horizontalLayout_7.addWidget(self.bmrInfoLabel)

        self.percentBmrFunctionLabel = QLabel(self.verticalLayoutWidget_8)
        self.percentBmrFunctionLabel.setObjectName(u"percentBmrFunctionLabel")

        self.horizontalLayout_7.addWidget(self.percentBmrFunctionLabel)

        self.percentSignLabel = QLabel(self.verticalLayoutWidget_8)
        self.percentSignLabel.setObjectName(u"percentSignLabel")

        self.horizontalLayout_7.addWidget(self.percentSignLabel)


        self.verticalLayout_12.addLayout(self.horizontalLayout_7)

        self.circleDiagramInfoLabel = QLabel(self.verticalLayoutWidget_8)
        self.circleDiagramInfoLabel.setObjectName(u"circleDiagramInfoLabel")

        self.verticalLayout_12.addWidget(self.circleDiagramInfoLabel)

        self.circleDiagramWidget = QGraphicsView(self.verticalLayoutWidget_8)
        self.circleDiagramWidget.setObjectName(u"circleDiagramWidget")

        self.verticalLayout_12.addWidget(self.circleDiagramWidget)


        self.verticalLayout_15.addLayout(self.verticalLayout_12)

        self.sportActivityButton = QPushButton(self.centralwidget)
        self.sportActivityButton.setObjectName(u"sportActivityButton")
        self.sportActivityButton.setGeometry(QRect(540, 600, 101, 41))
        self.resetFoodButton = QPushButton(self.centralwidget)
        self.resetFoodButton.setObjectName(u"resetFoodButton")
        self.resetFoodButton.setGeometry(QRect(20, 600, 111, 41))
        self.verticalLayoutWidget_9 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(10, 380, 641, 211))
        self.verticalLayout_16 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.barDiagramInfoLabel = QLabel(self.verticalLayoutWidget_9)
        self.barDiagramInfoLabel.setObjectName(u"barDiagramInfoLabel")

        self.verticalLayout_17.addWidget(self.barDiagramInfoLabel)

        self.barFoodDiagramWidget = QGraphicsView(self.verticalLayoutWidget_9)
        self.barFoodDiagramWidget.setObjectName(u"barFoodDiagramWidget")

        self.verticalLayout_17.addWidget(self.barFoodDiagramWidget)


        self.verticalLayout_16.addLayout(self.verticalLayout_17)

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar()
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.sexLabel.setText(QCoreApplication.translate("MainWindow", u"Sex", None))
        self.sexComboBoxWidget.setItemText(0, QCoreApplication.translate("MainWindow", u"Female", None))
        self.sexComboBoxWidget.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))

        self.heightLabel.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.cmLabel.setText(QCoreApplication.translate("MainWindow", u"cm", None))
        self.weightLabel.setText(QCoreApplication.translate("MainWindow", u"Weight", None))
        self.kgLabel.setText(QCoreApplication.translate("MainWindow", u"kg", None))
        self.ageLabel.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.yearOldLabel.setText(QCoreApplication.translate("MainWindow", u"years old", None))
        self.foodLabel.setText(QCoreApplication.translate("MainWindow", u"Food", None))
        self.foodAmountLabel.setText(QCoreApplication.translate("MainWindow", u"Food amount", None))
        self.unitFoodLabel.setText(QCoreApplication.translate("MainWindow", u"g/ml", None))
        self.confirmDataButton.setText(QCoreApplication.translate("MainWindow", u"Confirm data", None))
        self.chooseFoodLabel.setText(QCoreApplication.translate("MainWindow", u"Choose kind of 'Food' (entered above):", None))
        self.columnsFoodLabel.setText(QCoreApplication.translate("MainWindow", u"Full name, Type, Calories per 100g/ml, Kilojoules per 100g/ml", None))
        self.bmrLabel.setText(QCoreApplication.translate("MainWindow", u"Basal Metabolic Rate", None))
        self.countBmrFunctionLabel.setText("")
        self.calLabel.setText(QCoreApplication.translate("MainWindow", u"cal", None))
        self.caloriesInfoLabel.setText(QCoreApplication.translate("MainWindow", u"Calories in chosen food in entered amount: ", None))
        self.countAmountCaloriesLabel.setText("")
        self.calLabel_2.setText(QCoreApplication.translate("MainWindow", u"cal", None))
        self.bmrInfoLabel.setText(QCoreApplication.translate("MainWindow", u"Percentage amount of food calories in BMR: ", None))
        self.percentBmrFunctionLabel.setText("")
        self.percentSignLabel.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.circleDiagramInfoLabel.setText(QCoreApplication.translate("MainWindow", u"Circle diagram with all entered food types:", None))
        self.sportActivityButton.setText(QCoreApplication.translate("MainWindow", u"Sport activity", None))
        self.resetFoodButton.setText(QCoreApplication.translate("MainWindow", u"Reset foods", None))
        self.barDiagramInfoLabel.setText(QCoreApplication.translate("MainWindow", u"Daily consumed calories amount since last reset:", None))


app = QApplication(sys.argv)
gui = ui_MainWindow()
gui.show()
sys.exit(app.exec())