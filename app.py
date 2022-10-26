from flask import Flask
from query import exchanges_price
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def list():

   listPath = {"SearchExchange": "/BuyAndSaleExchange/<exchange>/<cryptomoneda>/<PriceUsdCop>",
               "SearchFullExchange": "/BuyAndSaleFull"}
   
   return escape(listPath)
    


@app.route("/BuyAndSaleExchange/<exchange>/<cryptomoneda>/<PriceUsdCop>")
def Exchange(exchange,cryptomoneda,PriceUsdCop=None):

   instance = exchanges_price()

   if PriceUsdCop == None:

      diccionario = {'Data':instance.dictionary(exchange, cryptomoneda)}
   
   else:

      diccionario = {'Data':instance.dictionary(exchange, cryptomoneda,PriceUsdCop)}


   return escape(diccionario)

@app.route("/BuyAndSaleFull")
def FullExchanges():

   instance = exchanges_price()
   list = []
   for x in instance.list_exchnges:

      list.append({f'{x}':instance.dictionary(x,instance.list_cripto[0])})

   return escape(list)


if __name__=='__main__':
   app.run(debug=False)