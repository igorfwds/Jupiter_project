import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("http://127.0.0.1:8000")
driver.maximize_window()

button = driver.find_element(By.ID, "login")
button.click()

email = driver.find_element(By.ID, "email")
email.send_keys("sele@nium.com")

password = driver.find_element(By.ID, "senha")
password.send_keys("sele")

login = driver.find_element(By.ID, "login")
login.click()

appointments = driver.find_element(By.ID, "agendamentos")
appointments.click()

time.sleep(5)

select = driver.find_element(By.XPATH, "//a[contains(@href, '/user-update/1')]")
select.click()