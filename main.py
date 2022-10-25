from fastapi import FastAPI
from query import exchanges_price

app = FastAPI()


@app.get("/BuyAndSaleExchange/")
async def Exchange(exchange:str="buda",cryptomoneda:str = "btc"):

   instance = exchanges_price()
   return {'Data':instance.dictionary(exchange, cryptomoneda)}

@app.get("/BuyAndSaleFull/")
async def FullExchanges():

   instance = exchanges_price()
   list = []
   for x in instance.list_exchnges:

      list.append({f'{x}':instance.dictionary(x,instance.list_cripto[0])})

   return list
