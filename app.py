from flask import Flask
from query import exchanges_price
from markupsafe import escape

app = Flask(__name__)


@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


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
   app.run()