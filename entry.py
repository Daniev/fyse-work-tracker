import readwrite as rw


class Entry():
    def __init__(self, date, hour, comment):
        self.allGood = True
        if self.checkDate(date):
            """date, number from 1-31"""
            self.date = int(date)
            print("Successfully added date...")
        else:
            print("Date not added...")
            self.allGood = False

        if self.checkHour(hour):
            "hour, number from 1-8"
            self.hour = int(hour)
            print("Successfully added hour...")
        else:
            print("Hour not added...")
            self.allGodd = False

        "comment, string"
        self.comment = comment

    def checkDate(self, date):
        # TODO type check int
        try:
            date = int(date)
        except ValueError:
            print("ERROR: Date entered was not an int, aborting...")
            return False

        if date < 1:
            print("ERROR: Invalid input, number must be more than 1")
            return False
        elif date > 31:
            print("ERROR: No month goes beyond 31... Invalid number")
            return False
        return True

    def checkHour(self, hour):
        # TODO type check int
        try:
            hour = int(hour)
        except ValueError:
            print("ERROR: hour is not an int! Aborting...")
            return False

        if hour < 0:
            print("WARNING: Negative hour numbers are not allowed!")
            return False
        elif hour > 8:
            print("WARNING: I don't believe you work that long in just one day!")
            return False
        return True


def storeEntry(entry):
    data = rw.readJSONFile("hours.json")
    newEntry = {"date": entry.date ,"hour": entry.hour, "comment": entry.comment}
    data.append(newEntry)
    rw.writeJSONFile("hours.json", data)
    return
