from pathlib import Path
from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


ROOT_FOLDER = Path(__file__).parent.parent.parent
CHROME_DRIVER_PATH = ROOT_FOLDER / 'bin' / 'chromedriver.exe'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=CHROME_DRIVER_PATH
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


def pesquisar(pesquisa: str):
    barra_pesquisa = chrome.find_element(
        By.CSS_SELECTOR,
        'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf >'
        ' form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
    botao_pesquisa = chrome.find_element(By.CSS_SELECTOR,
                                         'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > '
                                         'div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b')
    barra_pesquisa.send_keys(pesquisa)
    botao_pesquisa.click()


if __name__ == '__main__':
    palavra_pesquisa = str(input('o que deseja pesquisar? '))
    chrome = make_chrome_browser('--disable-gpu', '--no-sandbox')
    chrome.get('https://www.google.com.br')
    pesquisar(palavra_pesquisa)
    sleep(30)
    chrome.quit()
