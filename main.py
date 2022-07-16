"""Main file of project fysehours

should track: hour, comment, date (from user) and then calculate hours and pay for:
    this week, month, semester"""

# TODO date, gui (one page only)
import wx

import gui
import readwrite as rw
import startup as start


def main():
    if (start.firstTime()):
        start.makeFiles() 

    print ("Fetching data...")
    d_Hours = rw.readJSONFile("hours.json")
    d_Stats = rw.readJSONFile("stats.json")

    print ("Initializing window...")
    app = wx.App()
    gui.MyFrame()
    app.MainLoop()
    print("Exiting program...")


if __name__ == "__main__":
   main()
