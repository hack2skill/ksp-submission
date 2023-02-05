from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("window-size=600x300")
driver.get("https://ksp-vanchane-sample.azurewebsites.net")
time.sleep(2)

driver.find_element(By.XPATH, "//input[@name='email']").send_keys("validuser@email.com") 
time.sleep(1)
driver.find_element(By.XPATH, "//input[@placeholder='+91']").send_keys("+917894561230") 
time.sleep(1)
driver.find_element(By.XPATH, "//input[@name='psw']").send_keys("G00dp@ssw0rd") 
time.sleep(1)
driver.find_element(By.XPATH, "//input[@name='psw-repeat']").send_keys("G00dp@ssw0rd") 
time.sleep(1)

driver.find_element(By.CLASS_NAME, "signupbtn").click()

time.sleep(5)

driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[3]/div/div[1]/a").click()
time.sleep(5)

driver.find_element(By.XPATH, "//button[contains(text(),'add to cart')]").click()
time.sleep(5)

driver.find_element(By.XPATH, "//button[contains(text(),'go to cart')]").click()
time.sleep(5)

driver.find_element(By.XPATH, "//button[contains(text(),'Arrange call to proceed')]").click()
time.sleep(1000)
