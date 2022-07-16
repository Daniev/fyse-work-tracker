"""GUI makes the gui"""

import wx

import readwrite as rw
from entry import Entry, storeEntry


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="fysehours", size= wx.Size(800,600))
        self.makeContent()
        self.Show()
        
    def makeContent(self):
        """Makes all gui content"""
        vSizer = wx.BoxSizer(wx.VERTICAL)
        #if needed..
        hSizer = wx.BoxSizer(wx.HORIZONTAL) 
        
        # showing stats
        self.entryList = wx.ListView(self)
        #make entries..
        entries = rw.readJSONFile("hours.json") # list

        # button (to display popup to add more)
        addButton = wx.Button(self)
        addButton.SetLabelText("Add new")
        addButton.Bind(wx.EVT_BUTTON, self.makePopUp)
        purgeButton = wx.Button(self)
        purgeButton.SetLabelText("Purge")
        purgeButton.Bind(wx.EVT_BUTTON, self.purgeList)

        # Should be made unmutable
        self.InfoText = wx.TextCtrl(self)
        self.InfoText.SetValue("Here, info will appear...")
        elements = [addButton, purgeButton, self.InfoText]
        self._addToSizer(elements, vSizer)

        self.SetSizer(vSizer)
        return

    def makePopUp(self, event):
        """Allows user to enter hour, comment and date(maybe)"""
        self.dialog = wx.Dialog(self, size=wx.Size(400,400))
        dialogSizer = wx.BoxSizer(wx.VERTICAL)

        #Textctrls?
        textSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        dateInfo = wx.StaticText(self.dialog)
        dateInfo.SetLabelText("Input date: 1-31")
        self.inputDate = wx.TextCtrl(self.dialog)
        dates = [dateInfo, self.inputDate]
        self._addToSizer(dates, textSizer1)

        textSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hourInfo = wx.StaticText(self.dialog)
        hourInfo.SetLabelText("Input hours: 0-8")
        self.inputHours = wx.TextCtrl(self.dialog)
        hours = [hourInfo, self.inputHours]
        self._addToSizer(hours, textSizer2)

        textSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        commentInfo = wx.StaticText(self.dialog)
        commentInfo.SetLabelText("input comment here")
        self.inputComment = wx.TextCtrl(self.dialog)
        comments = [commentInfo, self.inputComment]
        self._addToSizer(comments, textSizer3)

        inputTexts = [textSizer1, textSizer2, textSizer3]
        self._addToSizer(inputTexts, dialogSizer)


        

        # buttons
        buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        submitButton = wx.Button(self.dialog)
        submitButton.SetLabelText("Submit")
        submitButton.Bind(wx.EVT_BUTTON, self.makeNewEntry)
        exitButton = wx.Button(self.dialog)
        exitButton.SetLabelText("Exit")
        exitButton.Bind(wx.EVT_BUTTON, self.exitDialog)
        buttons = [submitButton, exitButton] 
        self._addToSizer(buttons, buttonSizer)  
        hsizer = [buttonSizer]
        self._addToSizer(hsizer, dialogSizer)

        self.dialog.SetTitle("Add new fyse session")
        self.dialog.SetSizer(dialogSizer)
        self.dialog.Show()
        return


    def _addToSizer(self,elements, sizer):
        """Adds provided element to provided sizer."""
        for element in elements:
            sizer.Add(element, flag=wx.ALL | wx.EXPAND, border=8)   
        return

    def exitDialog(self, event):
        self.dialog.Destroy()
        return

    def makeNewEntry(self, event):
        """Stores the entry added"""
        date = self.inputDate.GetValue()
        hour = self.inputHours.GetValue()
        comment = self.inputComment.GetValue()
        print("Checking validity...")
        entry = Entry(date, hour, comment)
        # TODO store the entry...

        # if it passed the validity:
        if entry.allGood:
            print("Adding submitted event..")
            #precede...
            self._updateInfoTextTo("Adding submitted info...")
            storeEntry(entry)
            self._updateInfoTextTo("Successfully added new entry..")
            pass
        else:
            print("Wrong Input! Try again...")
            self._updateInfoTextTo("Wrong input! Try again...")
        
        self.dialog.Destroy()
        return

    def _updateInfoTextTo(self, newText):
        self.InfoText.SetValue(newText)
        return

    def purgeList(self, event):
        print("Purgin list")
        return

    def updateListView(self, newEntry):
        """Updates the listView by adding new data"""
        # data = rw.readJSONFile("entry.json")
        # append the newEntry to the list..
        # dislplay it in the list...
        return
