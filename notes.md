#FYSEHOURS
Program that allows user to track how much he works at his job
in an easy way.

TODO:
- feat: payment calculator to stats
- feat: display stats
- fix: Clean up when done..


* * *
#GUI:
## Main Window
Should contain the previously listed items,
an *addButton*  which makes the dialog, and a *delete/purge button*
when it is no longer needed. Also, add a textctrl called info, providing info messages 
by the program.
* * *
##Dialog
Pop up to add a new entry.
Should ask user for date (int from 1-31), hours and comment.

* * *
# Storage
Data are stored in json in the following format:
In hours.json:
[
{
    "date": 1-31,
    "hours": 1-8,
    "comment": string
  }
]

In stats.json
{
    "TotalSinceStart": int,
    "TotalThisSession": int,
    "BestDay": int
  }
Data validation is done when making a entry class instance...
