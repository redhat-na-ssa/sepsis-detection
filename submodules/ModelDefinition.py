import json

class SpecElement:

    def __init__(self,name,dataType,isRequired = False,isArray = False):
        self.name = name
        self.dataType = dataType
        self.isRequired = isRequired
        self.isArray = isArray

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()    



class ModelIO:

    def __init__(self,input = [],output = []):
        self.input = input
        self.output = output

    def addInputElement(self,element : SpecElement):
        self.input.append(element)   

    def addOutputElement(self,element : SpecElement):
        self.input.append(element)     

class ModelExporter:
   model : any
   spec: ModelIO

   def __init__(self,model,spec):
        self.model = model
        self.spec = spec