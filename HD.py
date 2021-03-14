from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import pathlib

email = str(input("email :"))
password = str(input("password :"))
contact = str(input("send to :"))
messageContent = str(input("your message :"))

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

#optinal, you can hide browser with headless chrome, uncomment if you like it that way
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)

driver = webdriver.Chrome(executable_path = "chromedriver", chrome_options=chrome_options)
driver.get("https://www.facebook.com/")

delay = 5

email = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='email']")))
email.click()
email.send_keys(email)

password = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='pass']")))
password.click()
password.send_keys(password)

submit = WebDriverWait(driver, delay*2).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")))
submit.click()

messanger = WebDriverWait(driver, delay*5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[2]/span/div/div[1]"))).click()

search = WebDriverWait(driver, delay*5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/label")))
search.click()
search.send_keys(contact)

contact = WebDriverWait(driver, delay*5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/ul/li[1]/ul/li[1]/div/a/div")))
contact.click()

message = WebDriverWait(driver, delay*5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/div")))
message.click()
message.send_keys(messageContent)
message.send_keys(Keys.RETURN)

time.sleep(5)
driver.close()