import sys
from PySide6.QtWidgets import QApplication
from UIControls.LandingScreenController import *

def main():
    app = QApplication(sys.argv)
    controller = LandingScreenController()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()