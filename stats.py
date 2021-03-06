"""Calculates stats"""
import readwrite as rw


def PAYRATE():
    """Constants used throughout"""
    return 170

def STATNUMBER():
    """Easy way to edit the number of stats if they should change.."""
    return 5

def getExistingStats():
        stats = rw.readJSONFile("stats.json") 
        return stats

def updateStats(entry):
    """Interface for other scripts"""
    stats = getExistingStats()
    stats = updateTotals(entry.hour, stats)
    stats = checkBestDay(entry.hour, stats)

    rw.writeJSONFile("stats.json", stats)
    return stats


def updateTotals(newNumber, stats):
    payRate = PAYRATE()
    stats["TotalSinceStart"] += newNumber
    stats["TotalThisSession"] += newNumber
    stats["PayTotal"] += newNumber * payRate
    stats["PayThisSession"] += newNumber * payRate
    return stats

def ResetSession(newNumber ):
    payRate = PAYRATE()
    stats = getExistingStats()
    stats["TotalThisSession"] = newNumber
    stats["PayThisSession"] = newNumber * payRate
    rw.writeJSONFile("stats.json",stats)
    return 

def checkBestDay(newNumber, stats):
    bestDay = stats["BestDay"]
    if newNumber > bestDay:
        stats["BestDay"] = newNumber
    return stats
