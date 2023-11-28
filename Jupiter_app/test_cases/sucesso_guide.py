import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


class CancelarConsultaTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://djangodeployjupiter.azurewebsites.net')
        time.sleep(3)

    def test_mensagem_exibida(self):
        # Navegar para a página inicial do paciente ou qualquer página relevante
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
        self.browser.get(
            'https://djangodeployjupiter.azurewebsites.net/homePaciente/')

    # Aguardar a renderização da página
        time.sleep(3)

    # Verificar se a mensagem está presente no HTML
    try:
        question_mark = self.browser.find_element(
            By.XPATH, '//*[contains(text(), "Essa é sua lista de consultas marcadas")]')
        question_mark.click()
        time.sleep(3)
        mensagem_element = self.browser.find_element(
            By.XPATH, '//*[contains(text(), "Essa é sua lista de consultas marcadas")]')
        self.assertTrue(mensagem_element.is_displayed(),
                        "Mensagem não encontrada ou não visível.")
        print("Mensagem encontrada:", mensagem_element.text)
    except Exception as e:
        print("Erro ao encontrar mensagem:", e)

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
