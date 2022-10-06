from selenium import webdriver
import undetected_chromedriver.v2 as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

#making chrome headless--No chrome browser UI launched
options = Options()
#options.add_argument("--headless")
options.add_argument("proxy-server=106.122.8.54:3128")
options.add_argument(r"--user-data-dir=C:\Users\hp\AppData\Local\Google\Chrome\User Data\Default")
# options.add_argument("disable-popup-blocking")
# options.add_argument("disable-notifications")

driver = uc.Chrome(options=options)

#getting the kilimal url to render dynamic data
URL = "https://bot.incolumitas.com/"
username_text = "gegerick"
email_text = "erickgege16@gmail.com"
delay = 0.6

driver.get(URL)
driver.maximize_window()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#userNameField > div > input")))
element = driver.find_element(By.CSS_SELECTOR, "#userNameField > div > input")

actions = ActionChains(driver)
actions.move_to_element(element).perform()

time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#userNameField > div > input").clear()
username_element = driver.find_element(By.CSS_SELECTOR, "#userNameField > div > input")
for c in username_text:
        endtime = time.time() + delay
        username_element.send_keys(c)
        time.sleep(endtime - time.time())

time.sleep(1)
email_textfield = "#emailField > div > input"
driver.find_element(By.CSS_SELECTOR, email_textfield).clear()
email_element = driver.find_element(By.CSS_SELECTOR, email_textfield)
for c in email_text:
        endtime = time.time() + delay
        email_element.send_keys(c)
        time.sleep(endtime - time.time())

time.sleep(1)
no_of_cookies_select = Select(driver.find_element(By.CSS_SELECTOR, "#formStuff > div:nth-child(3) > div > div > select"))
no_of_cookies_select.select_by_index(1)

time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#formStuff > div:nth-child(4) > div > label > input[type=checkbox]").click()
driver.find_element(By.CSS_SELECTOR, "#smolCat").click()
driver.find_element(By.CSS_SELECTOR, "#submit").click()

time.sleep(5)

#alert accepting
driver.switch_to.alert.accept()

score_result_selector = "#botScore > span"
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, score_result_selector)))
score_element = driver.find_element(By.CSS_SELECTOR, score_result_selector)
actions = ActionChains(driver)
actions.move_to_element(score_element).perform()
print(score_element.text)


time.sleep(5)
driver.quit()


# driver.find_element(By.CSS_SELECTOR, "#userNameField > div > input").clear()
# driver.find_element(By.CSS_SELECTOR, "#userNameField > div > input").send_keys("gegerick")