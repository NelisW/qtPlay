from PyQt5 import QtGui
from PyQt5 import QtWidgets as QtWidgets
from PyQt5.QtCore import QThread as QThread
from PyQt5.QtCore import pyqtSignal
import sys
import os

import subred

import urllib.request
import urllib.error

import json
import time


class getPostsThread(QThread):

    # create a new signal with payload of type str
    sigNewPost = pyqtSignal(str)

    def __init__(self, subreddits):
        """        Make a new thread instance with the list of subreddit names
        """
        # init base, avoid referring to the base class explicitly
        super().__init__()
        self.subreddits = subreddits

    def __del__(self):
        self.wait()

    def _get_top_post(self, subreddit):
        """Get string with top post title, author, and subreddit name for subreddit
        """
        url = "https://www.reddit.com/r/{}.json?limit=1".format(subreddit)
        headers = {"User-Agent": "nikolak@outlook.com tutorial code"}
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        data = json.load(response)
        top_post = data["data"]["children"][0]["data"]
        return "'{title}' by {author} in {subreddit}".format(**top_post)

    def run(self):
        """Internal thread event loop to fetch top post(s) and emit signal(s)
        """
        for subreddit in self.subreddits:
            # fetch top post
            top_post = self._get_top_post(subreddit)
            #  emit signal sigNewPost with string payload top_post
            self.sigNewPost.emit(top_post)
            # limit access to reddit to 1 access per two seconds
            self.sleep(2)


class ThreadingTutorial(QtWidgets.QMainWindow, subred.Ui_MainWindow):
    def __init__(self):
        # init base, avoid referring to the base class explicitly
        super().__init__()
        # calling function in subred to build GUI
        self.setupUi(self)
        # connect button signals to their events
        self.btn_start.clicked.connect(self.start_getting_top_posts)
        self.btn_exit.clicked.connect(self.exit)

    def start_getting_top_posts(self):
        # Get the subreddits user entered into an QLineEdit field

        subreddit_list = str(self.edit_subreddits.text()).split(",")
        # because ''.split(',') == ['']
        if subreddit_list == [""]:
            QtWidgets.QMessageBox.critical(
                self,
                "No subreddits",
                "You didn't enter any subreddits.",
                QtWidgets.QMessageBox.Ok,
            )
            return

        # progress bar, can be any int and it will be converted to x/100%
        self.progressBar.setMaximum(len(subreddit_list))
        # Setting the value on every run to 0
        self.progressBar.setValue(0)

        # Set up thread class with list of subreddits
        self.get_thread = getPostsThread(subreddit_list)

        # Connect the signal from the thread to display function
        # string pay load is automatically handled, no need to show here
        self.get_thread.sigNewPost.connect(self.add_post)

        #connect thread finish signal to notification function
        #we don't need to catch the terminated signal, but could
        self.get_thread.finished.connect(self.done)

        # We have all the events we need connected we can start the thread
        self.get_thread.start()
        # allow user to stop/terminate the thread, so we enable stop button
        self.btn_stop.setEnabled(True)
        # connect stop btn to the built in QThread terminate method
        self.btn_stop.clicked.connect(self.get_thread.terminate)
        # prevent user from starting another thread while this one is running
        self.btn_start.setEnabled(False)

    def add_post(self, post_text):
        """Add post text to list_submissions QListWidget
        """
        self.list_submissions.addItem(post_text)
        self.progressBar.setValue(self.progressBar.value() + 1)

    def done(self):
        """Show the message that fetching posts is done.
        """
        #disable stop button
        self.btn_stop.setEnabled(False)
        #enable start button
        self.btn_start.setEnabled(True)
        # reset progress bar
        self.progressBar.setValue(0)
        QtWidgets.QMessageBox.information(self, "Done!", "Done fetching posts!")

    def exit(self):
        QtWidgets.QApplication.quit()


def main():
    # create the app
    app = QtWidgets.QApplication(sys.argv)
    # using the class above
    form = ThreadingTutorial()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()

