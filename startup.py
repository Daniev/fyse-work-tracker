# Startup script
"""makes the files necessary to run the program at startup """
import os

import readwrite as rw


def firstTime():
    """Checks if this is the first time"""
    try:
        data = rw.readJSONFile("stats.json")
        print ("Skipping startup ...")
        return False
    except:
        print ("Running startup script...")
        return True


def makeFiles():
    """Makes all json files and loads them with initial content"""
    print ("Making files...")
    filepath = "files"
    isExisting = os.path.exists(filepath)
    if not isExisting:
            os.makedirs(filepath)
    hours = []
    stats = {"TotalSinceStart": 0,
            "TotalThisSession": 0,
            "BestDay":0,
            "PayTotal": 0,
            "PayThisSession": 0
            }
    rw.writeJSONFile("hours.json", hours)
    rw.writeJSONFile("stats.json", stats)


    
