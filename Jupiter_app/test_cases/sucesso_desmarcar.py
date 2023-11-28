import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CancelarConsultaTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://djangodeployjupiter.azurewebsites.net')
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, 10)
        time.sleep(3)

    def test_cancelar_consulta(self):
        try:
            # Realizar o login
            button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "login")))
            button.click()

            email = self.wait.until(
                EC.element_to_be_clickable((By.ID, "email")))
            email.send_keys("sele@nium.com")

            password = self.wait.until(
                EC.element_to_be_clickable((By.ID, "senha")))
            password.send_keys("sele")

            login = self.wait.until(
                EC.element_to_be_clickable((By.ID, "login")))
            login.click()

            # Aguardar um tempo suficiente após o login antes de prosseguir
            time.sleep(5)

            # Aguardar até que a página de agendamentos esteja carregada
            self.wait.until(EC.presence_of_element_located(
                (By.ID, "agendamentos")))

            # Navegar até a página de agendamentos
            appointments = self.wait.until(
                EC.element_to_be_clickable((By.ID, "agendamentos")))
            appointments.click()

            # Aguardar até que o botão de cancelamento seja visível
            cancel_button = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, '//a[@class="btn btn-danger rounded-3 p-2"]')))
            cancel_button.click()

            # Aguardar até que o campo de CPF seja visível
            cpf_input = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'input[name="cpf"]')))

            # Preencher o campo de CPF
            cpf_input.send_keys("123666")

            # Clicar no botão de confirmação de cancelamento
            confirm_button = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//button[@type="submit"]')))
            confirm_button.click()

            # Aguardar mensagem de confirmação (ajuste o XPath conforme necessário)
            success_message = self.wait.until(
                EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Consulta cancelada com sucesso!")]')))
            self.assertEqual(success_message.text,
                             'Consulta cancelada com sucesso!')
            print("Mensagem de sucesso encontrada:", success_message.text)

        except Exception as e:
            print("Erro durante a execução do teste:", e)
            raise  # Re-raise a exceção para que o teste seja marcado como falha

    def tearDown(self):
        self.browser.quit()


if __name__ == '_main_':
    unittest.main()
