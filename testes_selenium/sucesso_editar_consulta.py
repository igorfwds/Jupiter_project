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

WebDriverWait(driver, 7)

time.sleep(5)

select = driver.find_element(By.XPATH, "//a[contains(@href, '/user-update/4')]")
select.click()

doctor = driver.find_element(By.XPATH, "/html/body/main/div/form/div[1]/select/option[6]")
doctor.click()

date = driver.find_element(By.XPATH, "/html/body/main/div/form/div[2]/select/option[10]")
date.click()

time.sleep(4)
button = driver.find_element(By.XPATH, "/html/body/main/div/form/button[1]")
button.click()

app_time = driver.find_element(By.XPATH,"/html/body/main/div/form/div/select/option[3]")
app_time.click()

button = driver.find_element(By.XPATH, "/html/body/main/div/form/button")
button.click()