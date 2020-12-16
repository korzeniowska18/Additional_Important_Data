# $ install selenium

# $ brew cask reinstall chromedriver

# seleniumeasy.com

from selenium import webdriver
driver = webdriver.Firefox()
#driver.get("https://www.google.com/")
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

popUpwindow = driver.find_element_by_xpath('//*[@id="at-cv-lightbox-close"]')
popUpwindow.click()

messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys("Hej! Jak się masz?")
showMessageButton = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button')
showMessageButton.click()
InputfieldA = driver.find_element_by_xpath('//*[@id="sum1"]')
InputfieldA.send_keys('123')
InputfieldB = driver.find_element_by_xpath('//*[@id="sum2"]')
InputfieldB.send_keys('321')
TotalSumButton = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button')
TotalSumButton.click()
