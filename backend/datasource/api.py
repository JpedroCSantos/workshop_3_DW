import requests
from contracts.schema import ComprasSchema, GenericSchema
from typing import List
import pandas as pd

class APIColletor:
    def __init__ (self, schema):
        self._schema = None
        self._aws = None
        self._buffer = None
        self._schema = schema
        return
    
    def start(self, param):
        response = self.getData(param)
        if response is None: return {"ERROR": "Não Foi possivel consultar a API"}
        extract_data = self.extractData(response)
        transform_data = self.transform(extract_data)
        return transform_data
    
    def getData(self, param):
        if(param < 1): 
            return requests.get(f"http://127.0.0.1:8000/gerar_compra").json()
        else:
            return requests.get(f"http://127.0.0.1:8000/gerar_compras/{param}").json()
    
    def extractData(self, response):
        result: List[GenericSchema] = []
        for item in response:
            index = {}
            for key, value in self._schema.items():
                if type(item.get(key)) == value:
                    index[key] = item[key]
                else:
                    index[key] = None
            result.append(index)
        return result
    
    def transform(self, response):
        result = pd.DataFrame(response)
        return result