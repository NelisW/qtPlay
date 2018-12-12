from PyQt5 import QtGui
from PyQt5 import QtWidgets as QtWidgets
import sys
import os

#import the GUI code
import design


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        # avoid referring to the base class explicitly
        super().__init__() 
        # calling function on design to build GUI
        self.setupUi(self)
        # connect the browse button with the function to browse
        self.btnBrowse.clicked.connect(self.browse_folder)
        # connect the exit button with the exit function
        self.buttonExit.clicked.connect(self.exit)

    def exit(self):
        QtWidgets.QApplication.quit()

    def browse_folder(self):
        self.listWidget.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self,"Pick a folder")
        if directory:
            for file_name in os.listdir(directory): 
                self.listWidget.addItem(file_name)

def main():
    # create the app
    app = QtWidgets.QApplication(sys.argv)
    # using the class above
    form = ExampleApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
    
