import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time


class CancelarConsultaTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        # Substitua pela URL real da sua aplicação
        self.browser.get('https://djangodeployjupiter.azurewebsites.net')
        time.sleep(3)  # Ajuste conforme necessário

    def test_cancelar_consulta(self):
        # ... (código de navegação para a página de agendamentos ou qualquer página relevante)
        button = self.browser.find_element(By.ID, "login")
        button.click()

        email = self.browser.find_element(By.ID, "email")
        email.send_keys("sele@nium.com")

        password = self.browser.find_element(By.ID, "senha")
        password.send_keys("sele")

        login = self.browser.find_element(By.ID, "login")
        login.click()

        appointments = self.browser.find_element(By.ID, "agendamentos")
        appointments.click()

        # Encontrar e clicar no link ou botão de cancelamento
        cancel_button = self.browser.find_element(
            By.XPATH, '//a[@class="btn btn-danger rounded-3 p-2"]')
        cancel_button.click()

        # Aguardar mensagem de confirmação (ajuste o XPath conforme necessário)
        try:
            success_message = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Consulta cancelada com sucesso!")]')))
            self.assertEqual(success_message.text,
                             'Consulta cancelada com sucesso!')
            print("Mensagem de sucesso encontrada:", success_message.text)
        except Exception as e:
            print("Erro ao encontrar mensagem de sucesso:", e)

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
