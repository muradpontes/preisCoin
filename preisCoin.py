__author__ = "muradpontes"
__version__ = "0.2"

import json
import requests
from time import sleep
from rich import print
from rich.columns import Columns
from rich.panel import Panel
from rich.console import Console

console = Console()


class get_json:
    
    def __init__(self):
        self.json_data = None
        self.currency = None
        self.high = None
        self.low = None
        self.name = None
        self.bid = None
        self.ask = None
        self.var_bid = None
        self.choice = None
    
    def get_data(self):
        url = "https://economia.awesomeapi.com.br/json/all"
        with console.status("Connecting to server...", spinner='simpleDots') as status:
            response = requests.get(url)
            if response.status_code == 200:
                self.json_data = response.json()
            else:
                print("Failed to connect to server")
                return False
        return True
    
    def parse_data(self, currency):
        if currency in self.json_data:
            data = self.json_data[currency]
            self.currency = data['code']
            self.high = data['high']
            self.low = data['low']
            self.name = data['name']
            self.bid = data['bid']
            self.ask = data['ask']
            self.var_bid = data['varBid']
    
    def loop(self):
        currency = input("Enter the currency code (ex.: USD, DOGE): ").upper()
        if self.get_data():
            self.parse_data(currency)
            print(f"\n{self.name}")
            panel_data = f"[bold yellow]{self.currency}[/bold yellow][bold white] to [/bold white][bold yellow]BRL[/bold yellow]"
            panel = [Panel(panel_data)]
            columns = Columns(panel)
            console.print(columns)
            print(f"\nHigh: [bold red]{self.high}")
            print(f"Low: [bold green]{self.low}")
            print(f"Buy: [bold white]{self.bid}")
            print(f"Sell: [bold white]{self.ask}")
            print(f"Variation: [bold white]{self.var_bid}")
            
            while self.choice != '2':
                self.choice = str(input('\nDo you want to view another currency?\n1. Yes\n2. No\n\n'))
                if self.choice == '1':
                    system('cls || clear')
                    self.loop()
                elif self.choice =='2':
                    sleep(1)
                    print('Goodbye!')
                    sleep(0.5)
                    exit()
    
main = get_json()
main.loop()
