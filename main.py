from selenium import webdriver
# to use selenium in chrom
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.firefox.service import Service
import time
from selenium.webdriver.common.by import By
# in order to use the keyboard
from selenium.webdriver.common.keys import Keys

# # path of the chrome driver in the PC
# service = Service(r"C:\selen\chromedriver.exe")
# # create object (i call it 'driver') and give it the Service(///path///) we did above
# driver = webdriver.Chrome(service=service)
# # call the object i created above and give it the url of the website i want to open
# driver.get("https://advantageonlineshopping.com/#/")

# the same but for firefox browser
service1 = Service(r"C:\selen\geckodriver.exe")
driver1 = webdriver.Firefox(service=service1)
driver1.get("https://www.google.com/")
driver1.maximize_window()
# find the element line search of google
google_search_line = driver1.find_element(By.CSS_SELECTOR, ".gLFyf")
# write python in the search line
google_search_line.send_keys("python")
# click enter from the keyboard
google_search_line.send_keys(Keys.ENTER)
time.sleep(1)
# clean the search line
driver1.find_element(By.CSS_SELECTOR, "input.gLFyf").clear()
# write "1" in the search line
driver1.find_element(By.CSS_SELECTOR, "input.gLFyf").send_keys("1")
# click enter for searching
driver1.find_element(By.CSS_SELECTOR, "input.gLFyf").send_keys(Keys.ENTER)
time.sleep(1)

# # another way to click for search by clicking on the button
# search_button = driver1.find_element(By.CSS_SELECTOR, ".FPdoLc > center:nth-child(1) > input:nth-child(1)")
# search_button.click()

sport1 = driver1.find_element(By.CSS_SELECTOR, ".eKjLze > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > h3:nth-child(2)")
sport1.click()

driver1.back()

# # in case an element is not found - define 10 seconds timeout
# driver.implicitly_wait(10)
#
#

# # when the web opened (driver.get...) wait 8 sec then driver.close() will close the web
# time.sleep(8)
# driver.close()


