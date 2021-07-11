#importing webdriver from selenium framework
from selenium import webdriver

#importing enter key from keyboard
from selenium.webdriver.common.keys import Keys

#importing modules required for explict wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

from selenium.webdriver.firefox.webdriver import WebDriver

#my system specfic path to the chromedriver
PATH = "/home/justin/Drivers/chromedriver"

#picking what OS I want to use, with corresponding driver needed
driver = webdriver.Chrome(PATH)

#opening a website
driver.get("https://techwithtim.net")

#getting title of site
print(driver.title)

#searching for an element and adding information to it, and submitting
search = driver.find_element_by_class_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

time.sleep(5)


#waiting for an element to pop up
try:
    main = WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.ID, "main"))
    )

    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-title")
        print (header.text)
except:
    driver.quit()

#closing a webpage
#driver.close()

#quitting the broswer
#driver.quit()