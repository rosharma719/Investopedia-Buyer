import time
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


    
print("Enter email address")
email = input().strip()
print("Enter password:")
pwd = input().strip() 
print("Buy or sell?")
bs = input().strip()
print("Enter the ticker/stock (Program only clicks on the first result):")
ticker = input().strip()
print("Enter the number of shares:")
q = input().strip()

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#logging in 
driver.get("https://www.investopedia.com/auth/realms/investopedia/protocol/openid-connect/auth?client_id=finance-simulator&redirect_uri=https%3A%2F%2Fwww.investopedia.com%2Fsimulator%2Fportfolio&state=92a2c2dc-fc3c-4857-9f5f-d6907428c783&response_mode=fragment&response_type=code&scope=openid&nonce=c5dc6dba-e324-49b5-89ef-77fb318fe3ff")
driver.implicitly_wait(10)
element = driver.find_element(By. CSS_SELECTOR, "#username")
element.click()
element.send_keys(f"{email}")
driver.implicitly_wait(10)
element = driver.find_element(By. CSS_SELECTOR, "#password")
time.sleep(0.5)
element.send_keys(f"{pwd}")
time.sleep(0.5)
element = driver.find_element(By.CSS_SELECTOR, "#login")
element.click()
time.sleep(1)
driver.implicitly_wait(10)
element = driver.find_element(By.CSS_SELECTOR, "#app > div > main > div > div.v-bottom-navigation.global-bottom-nav.v-item-group.theme--dark.v-bottom-navigation--grow.v-bottom-navigation--fixed.primary.darken-4.primary--text.text--lighten-5 > a:nth-child(2) > span > span.v-icon.notranslate.v-icon--dense.theme--dark > svg")
element.click()
time.sleep(0.5)

#Entering the ticker 
element = driver.find_element(By.CSS_SELECTOR, "#app > div > main > div > div.trade-page.simulator-main__page-content > div.container.stock-trade-view-page > div:nth-child(1) > div.col-12.pb-0.col > div > div > div > div > div") #ticker lookup box
element.click()
driver.implicitly_wait(10)
action = ActionChains(driver)
action.send_keys(f"{ticker}", Keys.RETURN) #type in string
action.perform() #replace the dropdown thing when you switch out the ticker
element = driver.find_element(By.CSS_SELECTOR, "#app > div > main > div > div.trade-page.simulator-main__page-content > div.container.stock-trade-view-page > div:nth-child(1) > div.col-12.pb-0.col > div > div > div > div > div > div.v-menu__content.theme--light.menuable__content__active.v-autocomplete__content") #click autofill
element.click() #select autofill

if (bs == "sell"): 
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div/div[3]/div[2]/div[1]/div[2]/form/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/div[1]")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()
    driver.implicitly_wait(10)
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div/div[3]/div[2]/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div")
    element.click()

#Entering the quantity and moving onto the next element
time.sleep(0.5)
element = driver.find_element(By.CSS_SELECTOR, "#app > div > main > div > div.trade-page.simulator-main__page-content > div.container.stock-trade-view-page > div:nth-child(1) > div.col-12.pt-0.col > form > div:nth-child(1) > div > div:nth-child(2) > div > div")
driver.execute_script("arguments[0].scrollIntoView();", element)
driver.implicitly_wait(10)
time.sleep(0.5)
element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div/div[3]/div[2]/div[1]/div[2]/form/div[1]/div/div[2]/div/div/div/div/div/input")
driver.implicitly_wait(10)
action = ActionChains(driver)
action.move_to_element(element).perform()
time.sleep(0.5)
driver.implicitly_wait(10)
element.send_keys(f"{q}")
time.sleep(0.5)

#finishing the trade 
element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/main/div/div[3]/div[2]/div[1]/div[2]/form/div[3]/div/div[2]/button/span/span")
driver.implicitly_wait(10)
element.click()
time.sleep(0.5)
element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div/div[3]/div/div/div[2]/button/span/span")
driver.implicitly_wait(10)
element.click()

time.sleep(5)
driver.quit()