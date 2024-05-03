from fastapi import FastAPI
from faker import Faker
import random
import pandas as pd

app = FastAPI()
fake = Faker()

default_store_number = 11

@app.get("/gerar_compra")
async def gerar_compra():
    return [gerar_compra_aleatoria()]
    

@app.get("/gerar_compras/{numero_resgistros}")
async def gerar_compras(numero_resgistros: int):
    if numero_resgistros < 1 : return [gerar_compra_aleatoria()]
    else:
        compras = []
        for i in range(numero_resgistros):
            compras.append(gerar_compra_aleatoria())
        return compras

def gerar_compra_aleatoria():
    return {
        "client": fake.name(),
        "creditcard": {
            "provider": fake.credit_card_provider(),
            "number": fake.credit_card_number()
        },
        "ean": int(fake.ean()),
        "price":  round(float(random.uniform(0, 100)), 2),
        "store": default_store_number,
        "dateTime": fake.iso8601(),
        "clientPosition": fake.location_on_land()
    }
