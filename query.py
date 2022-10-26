import requests

class exchanges_price():

    def __init__(self):

        self.list_exchnges = ['buda',
                              'bitso']
        self.list_cripto = ['btc']

    def dictionary(self,exchange:str = 'buda',cryptomoneda:str='btc',UsdCop:str= 4800.00):

        UsdCop = float(UsdCop)


        if exchange == self.list_exchnges[0]:

            consulta = requests.get(f'https://criptoya.com/api/{exchange}/{cryptomoneda}/cop/1').json()

            diccionario = {'Exchange':exchange,
                           'Crypto': cryptomoneda,
                           'Buy': f"{consulta['ask']/UsdCop} USD",
                           'Sale': f"{consulta['bid']/UsdCop} USD"
                           }

            return diccionario

        elif exchange == self.list_exchnges[1]:

            consulta = requests.get(f' https://criptoya.com/api/bitso/{cryptomoneda}/usd/1').json()

            diccionario = {'Exchange': exchange,
                           'Crypto': cryptomoneda,
                           'Buy': f"{consulta['ask']} USD",
                           'Sale': f"{consulta['bid']} USD"
                           }

            return diccionario



#consulta = requests.get('http://127.0.0.1:5000/BuyAndSaleFull').json()





