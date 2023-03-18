from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("http://moodle.mitsgwalior.in/")
link = driver.find_element(By.LINK_TEXT,"Log in")
link.click()

driver.find_element(By.ID , "username").send_keys("2021mc6de")
driver.find_element(By.ID , "password").send_keys("Devendra12#")
driver.find_element(By.ID , "loginbtn").click()

time.sleep(60)  