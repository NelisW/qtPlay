# Using Qt Creator to build UI

Loosely based on  
    
    https://nikolak.com/pyqt-qt-designer-getting-started/


## Prerequisites

You need 
1. PyQt5 already in Anaconda.
1. Qt Designer is part of Qt Creator (huge Qt5 distribution here: http://download.qt.io/archive/qt/5.12/5.12.0/).
1. pyiuc5 should be available on the command line after installing the above.

## QtCreator and QtDesigner


QtCreator (huge Qt IDE) contains QtDesigner (GUI layout designer). If the Qt install was successful, look for QtDesigner in the Windows Start Menu, hidden deep inside the Qt folder. For creating the GUI, you only need QtDesigner, not the full QtCreator.

### Building Forms with QtDesigner

Once QtDesigner is open, it will present a dialog for a new form. Choose the `Main Window` option and click `Create`.  This should create an empty main window with the boiler plating for a menu and a status bar.

Towards the top right there is an Object Inspector that shows the object in the current window. Keep the central widget, but remove the menu and status bar, we don't need that now.  Resize the form by dragging its edges.

Now drag and drop from the "Widget Box" in Qt Designer a "List Widget" (not List View) widget and two "Push Button"s. Place the list widget towards the top of the window and the two buttons towards the bottom.
Test the form by in QtDesigner selecting the menu Form>Preview.  

Select both buttons and use the horizontal layout button (the three vertical bars) to place the buttons in a horisontal layout (which will stretch horizontally).  There should be a red rectangle around the buttons.

Select the button layout (red rectangle) and the list widget and select the vertical layout (three horizintal bars).  There should now be a red rectangle around all the components.

Study the Object Inspector and figure out the layout and component hierarchy.  If you have trouble placing an element by dragging it in main form you can also drag and drop it in Object Inspector window.

The objects added above stay in the same position and size if the window is resized.  To make them scale with the window, use the window layout functionality.  Right click on empty space on the form (or on the MainWindow entry in the Object Inspector) and select the Layout entry and selecy vertical or horizontal.  When you preview now, the three widgets should scale with the size of the window.

The widgets should now be named and default text given.  Select each of the widgets and look in the Property Editor.  
The QObject>objectName entry is the name to be used in the code.  
The QAbstractButton>text entry is the text shown in the botton face.  
Set the name and text values as follows:


| Widget | Name | Text|
| ---- | ---- | ---|
| List widget| listWidget| - |
| Left button | btnBrowse| Pick a folder|
| Right button  |buttonExit| Exit|

Save the GUI design to the name `design.ui`

### Adding Code to Forms

There are now two options to using the GUI: (1) access the ui directly from code or (2) convert the ui to Python code that can be imported into the application. Note that this code will be overwritten when the form changes, so don't make changes to the form's code.

Convert the ui form to Python code with

    pyuic5 design.ui -o design.py

This will create a Python file design.py that will create the GUI when executed.

Create a file with the following code to import yhe design.py file and then use it to create the GUI:

    from PyQt5 import QtGui
    from PyQt5 import QtWidgets as QtWidgets
    import sys
    import os

    import design

    class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
        def __init__(self, parent=None):
            super(ExampleApp, self).__init__(parent)
            self.setupUi(self)
            self.btnBrowse.clicked.connect(self.browse_folder)
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
        app = QtWidgets.QApplication(sys.argv)
        form = ExampleApp()
        form.show()
        app.exec_()


    if __name__ == '__main__':
        main()
    
For an explanation of what super does, see  
https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods  
https://stackoverflow.com/questions/222877/what-does-super-do-in-python  