from datasource.api import APIColletor
from contracts.schema import ComprasSchema, GenericSchema

api = APIColletor(ComprasSchema).start(20)

print(api)