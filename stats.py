"""Calculates stats"""
import readwrite as rw


def getExistingStats():
        stats = rw.readJSONFile("stats.json") 
        return stats

def updateStats(entry):
    """Interface for other scripts"""
    stats = getExistingStats()
    stats = updateTotals(entry.hour, stats)
    stats = checkBestDay(entry.hour, stats)

    rw.writeJSONFile("stats.json", stats)


def updateTotals(newNumber, stats):
    stats["TotalSinceStart"] += newNumber
    stats["TotalThisSession"] += newNumber
    return stats

def ResetSession(newNumber, stats):
    stats["TotalThisSession"] = newNumber

def checkBestDay(newNumber, stats):
    bestDay = stats["BestDay"]
    if newNumber > bestDay:
        stats["BestDay"] = newNumber
    return stats