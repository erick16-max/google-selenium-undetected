from selenium import webdriver
import undetected_chromedriver.v2 as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import time
import random

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
delay = random.random()

driver.get(URL)
driver.maximize_window()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#userNameField > div > input")))
element = driver.find_element(By.CSS_SELECTOR, "#userNameField > div > input")

startmove = driver.find_element(By.ID,"moreInfo");
ActionChains(driver).move_to_element(startmove).move_by_offset(50, 2).perform();


time.sleep(1)
username_element = driver.find_element(By.CSS_SELECTOR, "#userNameField > div > input")
username_str =  username_element.get_attribute('value')

ActionChains(driver).move_to_element(username_element).double_click(username_element).pause(1).send_keys(Keys.BACKSPACE).perform()
time.sleep(1)

for c in username_text:
        endtime = time.time() + delay
        username_element.send_keys(c)
        time.sleep(endtime - time.time())

time.sleep(1)
email_textfield = "#emailField > div > input"
driver.find_element(By.CSS_SELECTOR, email_textfield).clear()
email_element = driver.find_element(By.CSS_SELECTOR, email_textfield)
email_str =  username_element.get_attribute('value')

ActionChains(driver).move_to_element(email_element).double_click(email_element).pause(1).send_keys(Keys.BACKSPACE).perform()
time.sleep(1)

for c in email_text:
        endtime = time.time() + delay
        email_element.send_keys(c)
        time.sleep(endtime - time.time())

time.sleep(1)
no_of_cookies_select = Select(driver.find_element(By.CSS_SELECTOR, "#formStuff > div:nth-child(3) > div > div > select"))
no_of_cookies_select.select_by_index(1)

time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#formStuff > div:nth-child(4) > div > label > input[type=checkbox]").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#smolCat").click()
time.sleep(1)
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