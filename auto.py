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

driver.find_element(By.ID , "username").send_keys("Your Username")
driver.find_element(By.ID , "password").send_keys("Your Password")
driver.find_element(By.ID , "loginbtn").click()
# driver.find_element(By.ID, "label_3_15").click()
mycourse_cont = driver.find_element(By.ID, "inst559980").text #this line has been added to fetch the text from the specific ID, in this case, listing the names
print(mycourse_cont) #this will print the names
time.sleep(60)  
