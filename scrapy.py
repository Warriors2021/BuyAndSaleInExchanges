import requests

class search_usd():

    def QueryUsdCop(self):

        url = "https://dolar.wilkinsonpc.com.co/"

        result = requests.get(url).text

        search = result.find('sube-numero')

        result = result[search:search+40]

        numbers = ['0','1','2','3','4','5','6','7','8','9','.']

        dollar = ''

        for x in result:

            if x in numbers:
                dollar += x


        dollar = float(dollar)

        return dollar

    def QueryUsdArs(self):

        url = "https://www.estrategiasdeinversion.com/cotizaciones/divisas/usd-ars"

        result = requests.get(url).text

        search = result.find('"last-58711')

        result = result[search:search+60]
        result = result[12:]
        numbers = ['0','1','2','3','4','5','6','7','8','9','.']

        dollar = ''

        for x in result:
            if x in numbers:
                dollar += x

        dollar = float(dollar)

        return dollar



