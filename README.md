
# 🤖 Bot de login em multiplas contas

Um bot feito para comentar em multiplas contas, Totalmente automatizado ele pode efetuar login em mais de 100 contas sucessivamente, uma por uma.


## 🛠 Funcionalidades

- Abrir driver de navegador.
- Efetuar login.
- Verificar se usuario foi logado.
- Redirecionar para links de posts.
- Enviar comentarios, com intervalo de tempo diferentes.
- Efetuar logout.
- Uso de multiplas contas no bot.

## 🔗 Links uteis 

- [tutorial de instalação de drivers](https://www.selenium.dev/pt-br/documentation/webdriver/getting_started/install_drivers/)
- [geckodriver](https://github.com/mozilla/geckodriver)
- [chromedriver](https://chromedriver.chromium.org/downloads)
- [operadriver](https://github.com/operasoftware/operachromiumdriver/releases)

## ⚙️ Configuração

Passo 1° - Instale um navegador de um dos drivers disponibilizados no projeto (chrome, opera, firefox).
observação: recomendado uso do firefox.

Passo 2° - Troque o caminho do driver em seu arquivo main.py de acordo com o navegador instalado


```py
#firefox
 self.driver = webdriver.Firefox(service=Service("PATH"), options=webdriver.FirefoxOptions())
#chrome
 self.driver = webdriver.Chrome(service=Service("PATH"), options=webdriver.ChromeOptions())
#opera
 self.driver = webdriver.Opera(service=Service("PATH"))

```

Passo 3° - Instale a biblioteca [selenium](https://www.selenium.dev/selenium/docs/api/py/).

```bash
$ pip install selenium
```

Passo 4° - Altere a lista de emails e senhas em src/assets/accounts.json
```py
#seguir modelo abaixo

  {
        "email":"example@gmail.com",
        "password":"12345678"
  }
```


 

## 🚀 Tecnologias usadas
- python
- selenium
- drivers firefox, chrome e opera


## ⚙️ Execução 

```bash
$ python main.py
```
