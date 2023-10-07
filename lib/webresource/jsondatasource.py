""

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