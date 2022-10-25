import requests
from scrapy import search_usd

class exchanges_price():

    def __init__(self):

        self.instance1 = search_usd()
        self.list_exchnges = ['buda',
                              'bitso']
        self.list_cripto = ['btc']

    def dictionary(self,exchange:str = 'buda',cryptomoneda:str='btc'):

        UsdCop = self.instance1.QueryUsdCop()
        UsdArs = self.instance1.QueryUsdArs()

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







