# Startup script
import os

import readwrite as rw

"""makes files necessary to run at startup first time """


def firstTime():
    """Checks if this is the first time"""
    try:
        data = rw.readJSONFile("stats")
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
    stats = {}
    rw.writeJSONFile("hours.json", hours)
    rw.writeJSONFile("stats.json", stats)


    
