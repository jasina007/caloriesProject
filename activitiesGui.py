
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.resize(800, 544)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 771, 23))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sportActivityLabel = QLabel(self.horizontalLayoutWidget)
        self.sportActivityLabel.setObjectName(u"sportActivityLabel")

        self.horizontalLayout.addWidget(self.sportActivityLabel)

        self.sportActivityWidget = QLineEdit(self.horizontalLayoutWidget)
        self.sportActivityWidget.setObjectName(u"sportActivityWidget")

        self.horizontalLayout.addWidget(self.sportActivityWidget)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 60, 391, 291))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.chooseActivityLabel = QLabel(self.verticalLayoutWidget)
        self.chooseActivityLabel.setObjectName(u"chooseActivityLabel")

        self.verticalLayout.addWidget(self.chooseActivityLabel)

        self.columnsNameActivitiesLabel = QLabel(self.verticalLayoutWidget)
        self.columnsNameActivitiesLabel.setObjectName(u"columnsNameActivitiesLabel")

        self.verticalLayout.addWidget(self.columnsNameActivitiesLabel)

        self.sportActivityListWidget = QListWidget(self.verticalLayoutWidget)
        self.sportActivityListWidget.setObjectName(u"sportActivityListWidget")

        self.verticalLayout.addWidget(self.sportActivityListWidget)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(410, 60, 381, 291))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.averageSpeedLabel = QLabel(self.verticalLayoutWidget_2)
        self.averageSpeedLabel.setObjectName(u"averageSpeedLabel")

        self.verticalLayout_2.addWidget(self.averageSpeedLabel)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.currentSpeedLabel_2 = QLabel(self.verticalLayoutWidget_2)
        self.currentSpeedLabel_2.setObjectName(u"currentSpeedLabel_2")

        self.horizontalLayout_3.addWidget(self.currentSpeedLabel_2)

        self.speedUnitLabel = QLabel(self.verticalLayoutWidget_2)
        self.speedUnitLabel.setObjectName(u"speedUnitLabel")

        self.horizontalLayout_3.addWidget(self.speedUnitLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.speedSliderWidget = QSlider(self.verticalLayoutWidget_2)
        self.speedSliderWidget.setObjectName(u"speedSliderWidget")
        self.speedSliderWidget.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.speedSliderWidget)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(290, 370, 221, 80))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.estimatingTimeLabel = QLabel(self.verticalLayoutWidget_3)
        self.estimatingTimeLabel.setObjectName(u"estimatingTimeLabel")

        self.verticalLayout_5.addWidget(self.estimatingTimeLabel)

        self.countedTimeLabel = QLabel(self.verticalLayoutWidget_3)
        self.countedTimeLabel.setObjectName(u"countedTimeLabel")

        self.verticalLayout_5.addWidget(self.countedTimeLabel)

        self.foodTypesButton = QPushButton(self.centralwidget)
        self.foodTypesButton.setObjectName(u"foodTypesButton")
        self.foodTypesButton.setGeometry(QRect(20, 470, 101, 51))
        self.resetActivitiesButton = QPushButton(self.centralwidget)
        self.resetActivitiesButton.setObjectName(u"resetActivitiesButton")
        self.resetActivitiesButton.setGeometry(QRect(640, 470, 131, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.sportActivityLabel.setText(QCoreApplication.translate("MainWindow", u"Sport activity: ", None))
        self.chooseActivityLabel.setText(QCoreApplication.translate("MainWindow", u"Choose type of sport activity: ", None))
        self.columnsNameActivitiesLabel.setText(QCoreApplication.translate("MainWindow", u"Full name, Calories to burn per kg", None))
        self.averageSpeedLabel.setText(QCoreApplication.translate("MainWindow", u"Average speed during activity:", None))
        self.currentSpeedLabel_2.setText("")
        self.speedUnitLabel.setText(QCoreApplication.translate("MainWindow", u"km/h", None))
        self.estimatingTimeLabel.setText(QCoreApplication.translate("MainWindow", u"Estimating time to burn today's calories:", None))
        self.countedTimeLabel.setText("")
        self.foodTypesButton.setText(QCoreApplication.translate("MainWindow", u"Food types", None))
        self.resetActivitiesButton.setText(QCoreApplication.translate("MainWindow", u"Reset sport activities", None))
    # retranslateUi

