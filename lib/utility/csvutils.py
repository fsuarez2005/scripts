""

import csv

class CSVTable:
    
    lines = None
    uniqLines = None

    # -------------------------
    
    class Row:
        data = None
        def __init__(self,rowDict):
            self.data = rowDict
        
        def __hash__(self):
            text = ''.join( list( self.data.values() ) )
            return hash(text)
            
        def __str__(self):
            return ','.join( list( self.data.values() ))
    
    # -------------------------
    
    def __init__(self):
        self.lines = []
        self.uniqLines = []
        
    def uniqueLines(self):
        "Filters out unique lines"
        uniqSet = set()
        for r in self.lines:
            uniqSet.add(tuple(r.data.values()))
        
    def forEachLine(self,lambdaFunction):
        for n in self.lines:
            lambdaFunction(n)
    
    def readFile(self,filename):
        with open(filename,newline='') as csvfile:
            csvReader = csv.DictReader(csvfile,delimiter=',',quotechar='"')
            for row in csvReader:
                self.lines.append(self.Row(row))




