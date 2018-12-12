

# Using Threads in PyQt

## Overview

Loosely based on (but largely rewritten for PyQt5)  
https://nikolak.com/pyqt-threading-tutorial/

This project provides a simple app that fetches top posts from few different subreddits (subsections of reddit.com) while following API rules of 1 request per 2 seconds in an application that uses threads to separate the GUI from the threaded tasks.

Final project goal:

1. Allow user to enter n number of subreddit names into an line edit field, separated by a comma.
1. Have a list where post titles will be displayed.
1. Have a progress bar that updates as the number of fetched subreddits increases.
1. Allow user to cancel the updating at any time.

The form is already download as subred.ui

## `urllib` access to Reddit
The URL access task is implemented as a worker function `_get_top_post` in the thread class `getPostsThread`. 
The code requests from Reddit the details of the top post in a particular topic. This is done with the `urllib` requests, which returns json formatted data.  The json data is parsed and used in a formatted string for display.

## Thread Class `getPostsThread`

See http://pyqt.sourceforge.net/Docs/PyQt5/signals_slots.html for a good intro into 
PyQt signals (events) and slots (Python callables, e.g., functions).

The `getPostsThread` class is derived from the QThread class which was written to work nicely with the rest of the Qt system. 

1.  The class defines a signal member `sigNewPost = pyqtSignal(str)` which has a string as payloed. 

1. The `sigNewPost` signal is emitted in the `getPostsThread.run()` function.  The `run()` function is essentially an event loop, internal to the thread, that does some work and then raise signals when the work is complete.

1. The `sigNewPost` is connected to the `ThreadingTutorial.add_post` function, which adds the signal payload string to the `list_submissions` widget in the GUI.

## Class `ThreadingTutorial`

This class sets up the GuI, connects the signals to the slots and starts the process.

Note that the app has static setup (done once initially) and dynamic setup (done every time the `Start` button is clicked). 

1.  The static set up loads the GUI and connects the start and exit buttons.

2. The dynamic set up is initiated every time the start button is clicks. The following then happens:

    - Get the list of topics 
    - Instantiate the thread class with the list of topics
    - Connect the thread's signal `sigNewPost` to `ThreadingTutorial.add_post`. This can only be done once the thread class exists, so it cannot be done statically.
    - Connect the thread's finish signal to `ThreadingTutorial.done` to capture and display message.
    - Start the thread 
    - Connect the stop button to thread's terminate signal, so that we can stop the thread.
    - Some house keeping on enabling and disabling buttons.
