from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#explicit wait
#implicit wait 

url = 'https://earth.google.com/'
driver = webdriver.Firefox()

driver.get(url)
wait = WebDriverWait(driver, 15)
sleep(30)
launchEarthButton = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/nav[1]/ul[2]/li[2]/a/span')))
launchEarthButton.click()
sleep(60)
driver.quit()
