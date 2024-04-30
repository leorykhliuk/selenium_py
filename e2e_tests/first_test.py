from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get('https://the-internet.herokuapp.com/')

driver.implicitly_wait(0.8)

link = driver.find_element(By.XPATH, value='//li/a[text()="Inputs"]')

link.click()

title = driver.title
print(title)

if title == 'Input':
 print(True)
else:
 print(False)

driver.quit()