import urllib
import urllib.request
import json
import jsonpath_ng

# PURPOSE



# CLASSES

## JSONObject
### Returned by BaseJSONDataSource
### 

## BaseJSONDataSource
### 

## Book
### Contains book data independent of the source
### Should function like a data class or struct

## BookDataSource
### 

# ==================================================

class JSONObject:
    attributePaths = None
    data = None
    obj = None
    
    def __init__(self,/, data=None, attributePaths=None):
        self.data = data
        self.attributePaths = attributePaths
    
    def generateJSONObject(self):
        self.obj = json.loads(self.data)
        
    def getPath(self,path):
        jsonpath_expr = jsonpath_ng.parse(path)
        results = jsonpath_expr.find(self.obj)
        
        # path could result in multiple matches so return as a list
        return [match.value for match in results]
    
    def getAttributeValue(self,attributeName):
        if self.attributePaths == None:
            raise Exception('Attributes Paths not set in JSONObject')
        
        if attributeName in self.attributePaths:
            return self.getPath(self.attributePaths[attributeName])
        else:
            return None
    


class BaseJSONDataSource:
    attributePaths = {}
    
    def getJSONFromURL(self,url):
        jsonObj = JSONObject()
        jsonObj.attributePaths = self.attributePaths
        
        jsonObj.data = b''
        
        with urllib.request.urlopen( url ) as f:
            while line := f.readline():
                jsonObj.data += line
                
        jsonObj.generateJSONObject()

        return jsonObj

# ==================================================

class Book(JSONObject):
    def getTitle(self):
        return self.getAttributeValue('title')

# ==================================================

class Author(JSONObject):
    attributePaths = {
        'name' : '$.name'
    }

# ==================================================

class BookDataSource(BaseJSONDataSource):
    pass

# ==================================================s

class OpenLibraryDataSource(BookDataSource):
    baseURL = 'https://openlibrary.org'
    isbnBaseURL = baseURL +'/isbn/'
    jsonSuffix = '.json'
    
    # use JSONPath to link to common data
    attributePaths = {
        'title' : '$.title',
        'authors': None
    }
    
    
    def getBookJSONByISBN(self,isbn):
        url = self.isbnBaseURL + isbn + self.jsonSuffix
        jsonObj = self.getJSONFromURL( url )
        
        # cannot do downcasting in python
        # extract data from JSONObject and create Book
        
        book = Book(attributePaths=self.attributePaths)
        book.data = jsonObj.data
        book.generateJSONObject()
        
        return book
        
    def getAuthorsByRef(self,olref):
        # olref is part of a URL used by OpenLibrary
        jsonObj = self.getJSONFromURL(self.baseURL+olref+self.jsonSuffix)
        return jsonObj
    
    
    
    
