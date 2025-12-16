from time import sleep

#Задание №1:

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get(" https://www.example.com")

# print(f'Заголовок страницы: {driver.title}')

# driver.quit()

#Задание №2:

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("https://www.python.org/")

# driver.find_element(By.LINK_TEXT, "Donate").click()

# driver.quit()

#Задание #3:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")

search_box.send_keys(Keys.ENTER)

driver.quit()

