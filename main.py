"""Main file of project fysehours
------------------------------------------------------------------------
linter: pyright
single folder containing entry, gui, main, readwrite, startup, stats
all logic is implemented in the gui through event functions triggered by gui buttons.

files are stored in a created files directory
------------------------------------------------------------------------
should track: hour, comment, date (from user) and then calculate hours and pay for:
this week, month, semester
------------------------------------------------------------------------
"""

import wx

import gui
import startup as start


def main():
    # make files at first run
    if start.firstTime():
        start.makeFiles() 

    print ("Initializing window...")
    app = wx.App()
    gui.MyFrame()
    app.MainLoop()

    print("Exiting program...")


if __name__ == "__main__":
   main()
