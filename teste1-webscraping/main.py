import utils
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# Configurando o browser
url = "https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss"

driver = webdriver.Chrome()

print("\n\nAbrindo link...")
print("\n\nIsso pode demorar um pouco, por favor, aguarde...")

# abrindo url
driver.get(url)

# criando uma espera para carregar o conteúdo da página totalmente
wait = WebDriverWait(driver, 30)

try:
    print("\n\n Versão mais recente do TISS encontrada...")
    print("\n\nIsso pode demorar um pouco, por favor, aguarde...")

    # após a espera, irá procurar e clicar no elemento passado pelo xpath
    last_version_tiss = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="parent-fieldname-text"]/p[3]/a')
        )
    )
    last_version_tiss.click()

    print("\n\nExecutando página e recebendo o link do pdf...")

    # após a espera, irá verificar se existe a presença do elemento e pegar seu atributo href
    get_link = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="parent-fieldname-text"]/div/table/tbody/tr[1]/td[3]/a')
        )
    ).get_attribute("href")

    # com o atributo href em mãos, abrirá outra guia com a url encontrada no href
    driver.execute_script(f"window.open('{get_link}', '_blank')")

finally:
    # com o link do pdf, irá executar o download e fechar o driver
    utils.download_pdf(get_link)
    driver.quit()
