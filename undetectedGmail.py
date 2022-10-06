from selenium import webdriver
import undetected_chromedriver.v2 as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#making chrome headless--No chrome browser UI launched
options = Options()
#options.add_argument("--headless")
options.add_argument("proxy-server=106.122.8.54:3128")
options.add_argument(r"--user-data-dir=C:\Users\hp\AppData\Local\Google\Chrome\User Data\Default")

#setting chrome as the web driver to use

driver = uc.Chrome(options=options)

#getting the kilimal url to render dynamic data
URL = "https://accounts.google.com/v3/signin/identifier?dsh=S1896193045%3A1664795538914883&continue=https%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWqq_dXCFITAnYAQbkLFM0EZkLTEEXfYB5p5k8zXCKILs5OB50VVsMJIa1VirutY9hTCUYcU6A"
driver.get(URL)

driver.find_element(By.ID,"identifierId").send_keys("philipgege8@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#identifierNext > div > button > span").click()

password_selector = "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input"

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, password_selector)))
driver.find_element(By.CSS_SELECTOR, password_selector).send_keys("Mazeras004")
driver.find_element(By.CSS_SELECTOR, "#passwordNext > div > button > span").click()

accounts_selector = "#gbwa > div > a"
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, accounts_selector)))
driver.find_element(By.CSS_SELECTOR, accounts_selector).click()

print("success")