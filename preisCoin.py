__author__ = "ohhhio"
__version__ = "0.1"

# imports
from rich import print
from rich.columns import Columns
from rich.panel import Panel
from rich.console import Console
from os import system
from time import sleep
import json
import urllib.request

# set console
console = Console()

# class to parse json data
class GetJSON:
    
    def __init__(self, get_json, moeda, maximo, minimo, nome, compra, venda, variacao, data, choice): # fix
        self.get_json = get_json
        self.moeda = moeda
        self.maximo = maximo
        self.minimo = minimo
        self.nome = nome
        self.compra = compra
        self.venda = venda
        self.variacao = variacao
        self.data = data
        self.choice = choice

    # get json from awesomeAPI
    def get_data(self):
        urlData = "https://economia.awesomeapi.com.br/json/all"
        webUrl = urllib.request.urlopen(urlData)
        with console.status("Conectando-se ao servidor...", spinner='simpleDots') as status:
            sleep(1.4)
            try:
                if (webUrl.getcode() == 200):
                    self.data = webUrl.read()
            except:
                print("Não foi possível conectar-se ao servidor") # fix
    
    # set variables
    def parse_data(self, coin):
        self.get_json = json.loads(self.data)

        if "name" in self.get_json[f"{coin}"]:
            self.moeda = self.get_json[f"{coin}"]
            self.maximo = self.moeda["high"]
            self.minimo = self.moeda["low"]
            self.nome = self.moeda["name"]
            self.compra = self.moeda["bid"]
            self.venda = self.moeda["ask"]
            self.variacao = self.moeda["varBid"]
    
    # show results
    def print_data(self, coin):
        
        while self.choice != '2':
            print(f"[bold white]\n{self.nome}")

            data = f"[bold yellow]{coin}[/bold yellow][bold white] to [/bold white][bold yellow]BRL"  
            painel = [Panel(data)]
            caixa = Columns(painel)
            console.print(caixa)

            print(f"\nMáxima: [bold red]{self.maximo}")
            print(f"\nMínima: [bold green]{self.minimo}\n")
        
            data = f"[bold yellow]Compra: [/bold yellow][bold white]{self.compra}[/bold white]\n[bold yellow]Venda: [/bold yellow][bold white]{self.venda}\n[bold yellow]Variacao: [bold white]{self.variacao}"
            painel = [Panel(data)]
            caixa = Columns(painel)
            console.print(caixa)
    
            choice = str(input('\nDeseja ver a cotação de outra moeda?\n1. Sim\n2. Não\n\n'))
            
            if choice == '1':
                system('cls || clear')
                main.loop()

            elif choice =='2':
                sleep(1)
                print('Até mais!')
                sleep(0.5)
                exit()
    
    # loop to view other coins
    def loop(self):
        moeda = input("Digite a moeda desejada (ex.: USD, DOGE): ").upper()
        main.get_data()
        main.parse_data(moeda)
        main.print_data(moeda)

# initiates
main = GetJSON(0, 0, 0, 0, 0, 0, 0, 0, 0, 0) # fix
main.loop()
