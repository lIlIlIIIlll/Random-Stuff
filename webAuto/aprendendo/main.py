from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

OPP = Options()
OPP.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=OPP)
wait = WebDriverWait(driver,5)

driver.get("https://senaiweb6.fieb.org.br/FRAMEHTML/web/app/edu/PortalEducacional/login/")
driver.maximize_window()
time.sleep(5)
inputs = driver.find_element(By.ID,"User").send_keys('023.927292')
inputs = driver.find_element(By.ID,"Pass").send_keys('828348')
inputs = driver.find_element(By.XPATH,'//input[@type="submit"]').click()
time.sleep(23)
inputs = driver.find_element(By.ID,"show-menu").click()
inputs = driver.find_element(By.ID,"EDU_PORTAL_FINANCEIRO").click()
time.sleep(3)
inputs = driver.find_element(By.ID,"controller_situacaoselecionada").click()
inputs = driver.find_element(By.XPATH,'//option[@value="3"]').click()
inputs = driver.find_element(By.ID,"controller_situacaoselecionada").click()



