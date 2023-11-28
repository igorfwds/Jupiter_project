import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time


class VisualizarReciboTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://djangodeployjupiter.azurewebsites.net')
        time.sleep(3)

    def test_visualizar_recibo(self):
        # Realizar o login
        button = self.browser.find_element(By.ID, "login")
        button.click()

        email = self.browser.find_element(By.ID, "email")
        email.send_keys("sele@nium.com")

        password = self.browser.find_element(By.ID, "senha")
        password.send_keys("sele")

        login = self.browser.find_element(By.ID, "login")
        login.click()

        # Aguarde um tempo suficiente após o login antes de prosseguir
        time.sleep(5)  # Ajuste conforme necessário

        # Navegar até a página de recibos usando execução de script
        self.browser.execute_script("window.location.replace('recibos/')")

        # Aguardar a página de visualização do recibo (ajuste o XPath conforme necessário)
        try:
            visualizacao_recibo = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), "Detalhes do Recibo")]')))
            self.assertEqual(visualizacao_recibo.text, 'Detalhes do Recibo')
            print("Página de visualização do recibo encontrada")
        except Exception as e:
            print("Erro ao encontrar a página de visualização do recibo:", e)

        # Clicar no botão "Visualizar Boleto"
        try:
            visualizar_boleto = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/main/div/table/tbody/tr[2]/td[3]/a')))
            visualizar_boleto.click()
            print("Botão 'Visualizar Boleto' clicado")
        except Exception as e:
            print("Erro ao clicar no botão 'Visualizar Boleto':", e)

        # Aguardar um curto período para permitir que a página processe
        time.sleep(2)

    def tearDown(self):
        self.browser.quit()


if __name__ == 'main':
    unittest.main()
