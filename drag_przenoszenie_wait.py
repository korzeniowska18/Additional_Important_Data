from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

skad = driver.find_element_by_xpath('//*[@id="box6"]')
dokad = driver.find_element_by_xpath('//*[@id="box106"]')
actions = ActionChains(driver)
actions.drag_and_drop(skad, dokad).perform()
sleep(10)



driver.close()










