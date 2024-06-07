# 
# 
# 




__all__ = ['Journal','JournalDirectory']

import os
import sys
import glob
import re
import datetime

JOURNAL_PREFIX = "journal"


class DirectoryStack:
    stack = []
    
    def __init__(self):
        self.stack = []
    
    def push(self,newdir):
        this.stack.append(os.curdir)
        
        # TODO: check for errors
        os.chdir(newdir)
    
    def pop(self):
        # check if stack is empty
        lastDir = self.stack.pop()
        
        os.chdir(lastDir)
    
class Journal:
    ""
    fileext = "pages"
    fileprefix = "journal"
    
    
    
    
    def __init__(self,path = None):
        self.path = path
        self.filenamePattern = '.*'+JOURNAL_PREFIX+'(\\d{4})(\\d{2})(\\d{2}).pages$'
    
    @classmethod
    def location_pattern(cls,journalPrefix,year,month,day):
        s =  f"{journalPrefix}{year}/"
        s += f"{journalPrefix}{year}{month}/"
        s += f"{journalPrefix}{year}{month}{day}.pages"
        return s
    
    def correct_location(self):
        dateObj = self.encoded_date()
        if dateObj is None:
            return None
        
        year = dateObj.strftime("%Y")
        month = dateObj.strftime("%m")
        day = dateObj.strftime("%d")
        
        return self.location_pattern(JOURNAL_PREFIX,year,month,day)
    
    def is_correct_location(self):
        #print(f"Path: {self.path}")
        #print(f"Correct Location: {self.correct_location()}")
        return self.path == self.correct_location()
    
    def dirname(self):
        return os.path.dirname(self.path)
    
    def basename(self):
        return os.path.basename(self.path)
    
    def is_journal(self):
        """Returns true if filename is of a journal file.
        
        Does not need to be in correct location.
        """
        
        # true if all of the following:
        #  filename follows pattern
        pattern = re.compile(self.filenamePattern)
        m = pattern.match(self.basename())
        if m is None:
            return False
        #  file exists
        return True


    def is_good(self):
        isjournal = self.is_journal()
        
        iscorrectlocation = self.is_correct_location()
        #return False
        return (isjournal and iscorrectlocation)

    # TODO: 
    def can_move(self):
        # check for file in correct location
        if (self.is_good()):
            return
        
        
        
        # get correct location for this journal
        correctlocation = self.correct_location()
        
        
        # check if this journal is in wrong location
        
        
        # check for existing file in location
        
        return False
    
    def encoded_date(self):
        "Returns data encoded into filename"
        
        pattern = re.compile(self.filenamePattern)
        m = pattern.match(self.basename())
        if m is not None:
            year = int(m.group(1))
            month = int(m.group(2))
            day = int(m.group(3))
            
            d = datetime.date(year,month,day)
        else:
            d = None
        
        return d
    def csv_string(self):
        return f"{self.path}\t{self.correct_location()}"


class JournalDirectory:
    # journals
    # dirstack
    # home_directory
    
    def __init__(self,home_directory):
        self.home_directory = home_directory
        self.dirstack = DirectoryStack()
        self.journals = []
    
    def glob_journals(self):
        # NOTE: need recursive for globstar to get all files
        filelist = glob.glob("**/*.pages",root_dir=self.home_directory,recursive=True)
        m = map(lambda f: Journal(f),filelist)
        self.journals = list(m)
        
    def fullpath(self,journal):
        p =  self.home_directory
        p += os.sep
        p += journal.path
        
        return p
    
    def good_journals(self):
        fo = filter(lambda j: j.is_good(),self.journals)
        return list(fo) 
    
    def bad_journals(self):
        fo = filter(lambda j: not j.is_good(),self.journals)
        return list(fo)
        
        
        
        
        
