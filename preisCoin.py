__author__ = "muradpontes"
__version__ = "0.3"

import requests
from rich.columns import Columns
from rich.panel import Panel
from rich.console import Console

console = Console()

class GetJSON:
    def __init__(self):
        self.data = None

    def get_data(self):
        url = "https://economia.awesomeapi.com.br/json/all"
        response = requests.get(url)
        if response.ok:
            self.data = response.json()
        else:
            print("Could not fetch data from server.")

    def print_coins(self):
        coins = self.data.keys()
        print("available coins:\n")

        columns = []
        for coin in coins:
            panel = Panel(coin, style="yellow on black")
            columns.append(panel)
        console.print(Columns(columns))

    def parse_data(self, coin):
        self.moeda = self.data[coin]
        self.nome = self.moeda["name"]
        self.compra = self.moeda["bid"]
        self.venda = self.moeda["ask"]
        self.maximo = self.moeda["high"]
        self.minimo = self.moeda["low"]
        self.variacao = self.moeda["varBid"]
    
    def print_data(self):
        print(f"\n{self.nome}")
        
        data = f"{self.moeda['code']} to BRL"
        painel = [Panel(data)]
        caixa = Columns(painel)

        console = Console()

        console.print(caixa)

        print(f"\nMax: {self.maximo}")
        print(f"\nMin: {self.minimo}\n")
        
        data = f"Buy: {self.compra}\nSell: {self.venda}\nVariation: {self.variacao}"
        painel = [Panel(data)]
        caixa = Columns(painel)
        console.print(caixa)
    
    def loop(self):
        self.get_data()
        self.print_coins()
        coin = input("Enter the coin to check: ").upper()
        while coin not in self.data:
            coin = input("Invalid coin, enter the coin to check: ").upper()
        self.parse_data(coin)
        self.print_data()

def main():
    get_json = GetJSON()
    print("welcome to preisCoin v0.3\n")

    while True:
        get_json.loop()

if __name__ == '__main__':
    main()
