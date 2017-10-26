from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

#open new firefox window and go to upwork login
driver = webdriver.Firefox()
driver.get("https://www.upwork.com/ab/account-security/login")

#wait for load
time.sleep(2)

#type email
user = driver.find_element_by_id("login_username")
user.send_keys("username")

#type password
password = driver.find_element_by_id("login_password")
password.send_keys("password")

#wait 2 seconds to click login
time.sleep(2)

#click login button
login = driver.find_element_by_class_name("btn.btn-block.btn-primary.p-lg-left-right")
login.click()

#wait for load
time.sleep(2)

#move to task list
driver.get("https://www.upwork.com/taskmanager/project/747846727908102144/tasks/list")
time.sleep(2)

x = 0
while (x < 20):
    try:
        claim = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-default.claim-btn")))
        claim.click()
        time.sleep(1)
        driver.get("https://www.upwork.com/taskmanager/project/747846727908102144/tasks/list")
        x = x + 1
    except TimeoutException:
        time.sleep(20)
        driver.refresh()

driver.quit()
