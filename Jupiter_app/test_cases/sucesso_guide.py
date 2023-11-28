import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class LoginMessageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://djangodeployjupiter.azurewebsites.net')

    def test_login_message(self):
        # Navigate to the login page
        self.browser.get('https://djangodeployjupiter.azurewebsites.net')

        # Wait for the page to load
        time.sleep(3)

        # Locate the element containing the message
        message_element = self.browser.find_element(
            By.XPATH, '//button[@onclick="window.alert(\'Essa é a tela de login, preencha com os campos de e-mail e senha com os dados registrados no momento do cadastro. Se ainda não possui cadastro, clique no ícone do canto superior esquerdo e procure o botão CADASTRE-SE\')"]')

        # Get the text of the element
        message_text = message_element.get_attribute('onclick')

        # Assert that the message is present
        self.assertIn('Essa é a tela de login, preencha com os campos de e-mail e senha com os dados registrados no momento do cadastro. Se ainda não possui cadastro, clique no ícone do canto superior esquerdo e procure o botão CADASTRE-SE', message_text)

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
