from selenium.webdriver.firefox.service import Service;
from src.services import login, logout, sendComentary
from selenium import webdriver
import json



class Client:
    def __init__(self, post, message):
        self.driver = webdriver.Firefox(service=Service("D:/Sistema/objetos 3D/programação/pythonBot/src/drivers/geckodriver.exe"), options=webdriver.FirefoxOptions())
        self.loggedNotAccounts = 0
        self.username = 'username'
        self.password = 'password'
        self.loggedAccounts = 0
        self.message = message
        self.commentsSent = 0
        self.post = post


    def run(self):
        with open('src/assets/accounts.json', 'r', encoding='utf-8') as f:
            accounts = json.load(f)

            for user in accounts:
         
                 if 'email'in user and 'password' in user:
                
                    self.username = user['email']
                    self.password = user['password']
                    checkUserLogged = login.run(self)
                    if checkUserLogged == 'user not logged': 
                        self.loggedNotAccounts += 1
                        print('[' + self.username + '] - Erro ao logar')
                    else: 
                        self.loggedAccounts += 1
                        print('[' + self.username + '] - Usuario logado')
                        commentarys = sendComentary.run(self)
                        self.commentsSent += commentarys
                        logout.run(self)
        


post = input('Insira abaixo a URL da postagem:\nr:  ')
message = input('Qual a mensagem a ser enviada?\nr:  ')



bot = Client(post, message)
bot.run()
