#!python3

# Journal Directory Structure
# Year -,----Month
#.      |
#       |
#       |---Month
#.      |
#.      |
#.      '---Month

from pathlib import Path
import datetime


journalBaseDirectory = Path('/Users/franksuarez/Library/Mobile Documents/com~apple~Pages/Documents/journal')
journalFilenamePattern = 'journal*.pages'


class Journal:
    filename = None
    date = None
    
    def __init__(self):
        pass

    def __init__(self,filename):
        self.filename = filename
        self.calculateDateFromFilename()
    
    def calculateDateFromFilename(self):
        # journalYYYYMMDD.pages
        datetimeformat = 'journal%Y%m%d.pages'
        self.date = datetime.datetime.strptime(self.filename,datetimeformat)
    
    def isFromYear(self,year):
        return (year == self.date.year)
        
    def isFromMonth(self,month):
        return (month == self.date.month)


def makeSortedPath(year,month):
    yearStr = f'{year:04d}'
    monthStr = f'{month:02d}'
    
    newPath = journalBaseDirectory / f'journal{yearStr}' / f'journal{yearStr}{monthStr}'
    print(newPath.exists())
    

def listAllJournals( ):
    journals = journalBaseDirectory.glob( '**/'+journalFilenamePattern )
    return journals

def checkJournalLocation(journalPathObj):
    location = journalPathObj
    print(location)
    
def test1():
    journals = listAllJournals()
    
    for j in journals:
        checkJournalLocation(j)

makeSortedPath(2)


#test1()

