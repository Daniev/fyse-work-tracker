"""Reads and write to json files with the functions here.."""

import json


def readJSONFile(file):
    filePath = "files/" + file
    with open (filePath, "r") as jsonfile:
        data = json.load(jsonfile) 
    return data

def writeJSONFile(file, data):
    filePath = "files/" + file
    with open (filePath, "w") as jsonfile:
       json.dump(data, jsonfile, indent=4)

def createJSONFile(file):    
    """Creates empty jsonfile"""
    filePath = "files/" + file
    data = {}
    with open(filePath, "w") as jsonfile:
        json.dump(data, jsonfile, indent=4)
