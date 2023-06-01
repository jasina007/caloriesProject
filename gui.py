import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QHBoxLayout, QVBoxLayout

class CaloriesAndActivities(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calories project')
        
        
        
        
        
        self.userDataLayout = QHBoxLayout()
        
        
        
app = QApplication(sys.argv)
window = QMainWindow()
window.show()
app.exec()