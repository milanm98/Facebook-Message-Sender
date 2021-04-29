from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

try:
    f = open("assets.txt")
    file = f.readlines()
    emailInput = file[0]
    passwordInput = file[1]
    
    emailInput = emailInput.strip()
    passwordInput = passwordInput.strip()

    contactInput = str(input("send to :"))
    messageContent = str(input("your message :"))

except IOError:
    with open("assets.txt", "w") as f:
        emailInput = str(input("email :"))
        passwordInput = str(input("password :"))
        contactInput = str(input("send to :"))
        messageContent = str(input("your message :"))

        f.writelines(emailInput + " \n")
        f.writelines(passwordInput + " \n")

        f.close()

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
email.send_keys(emailInput)

password = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='pass']")))
password.click()
password.send_keys(passwordInput)

submit = WebDriverWait(driver, delay*2).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")))
submit.click()

search = WebDriverWait(driver, delay*5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/label/input")))
driver.execute_script("arguments[0].click();", search)
search.send_keys(contactInput)

profile = WebDriverWait(driver, delay*5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div[2]/ul/li[1]/div/a/div/div[2]/div")))
profile.click()

openMessageBox = WebDriverWait(driver, delay*7).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/span/div[2]/span/span")))
openMessageBox.click()

messageBox = WebDriverWait(driver, delay*7).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/div")))
messageBox.click()
messageBox.send_keys(messageContent)
time.sleep(3)
messageBox.send_keys(Keys.RETURN)

time.sleep(5)
driver.close()