from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(r"C:\selen\geckodriver.exe")
drive = webdriver.Firefox(service=service)
drive.get("https://www.rail.co.il/")
drive.maximize_window()

from_line = drive.find_element(By.CSS_SELECTOR, "div.col-md-2:nth-child(2) > div:nth-child(2) > input:nth-child(1)")
from_line.send_keys("אשקלון")
from_line.send_keys(Keys.ENTER)

to_line = drive.find_element(By.CSS_SELECTOR, "div.col-md-2:nth-child(4) > div:nth-child(2) > input:nth-child(1)")
to_line.send_keys("בנימינה")
to_line.send_keys(Keys.ENTER)

drive.find_element(By.CSS_SELECTOR, "div.col-md-2:nth-child(7) > button:nth-child(1)").click()