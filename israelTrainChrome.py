from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

googDrive = webdriver.Chrome(executable_path=r"C:\selen\chromedriver.exe")
googDrive.get("https://www.rail.co.il/")
googDrive.maximize_window()

googDrive.find_element(By.CSS_SELECTOR, "#trainSearchMain > div > div > div > div.col-md-2.col-sm-5.col-xs-10.fromBox > div.typeahead.ng-isolate-scope > input").send_keys("אשקלון")
googDrive.find_element(By.CSS_SELECTOR, "#trainSearchMain > div > div > div > div.col-md-2.col-sm-5.col-xs-10.fromBox > div.typeahead.ng-isolate-scope > input").send_keys(Keys.ENTER)

googDrive.find_element(By.CSS_SELECTOR, "#trainSearchMain > div > div > div > div.col-md-2.col-sm-5.col-xs-10.toBox > div.typeahead.ng-isolate-scope > input").send_keys("בנימינה")
googDrive.find_element(By.CSS_SELECTOR, "#trainSearchMain > div > div > div > div.col-md-2.col-sm-5.col-xs-10.toBox > div.typeahead.ng-isolate-scope > input").send_keys(Keys.ENTER)

googDrive.find_element(By.CSS_SELECTOR, "#trainSearchMain > div > div > div > div.col-md-2.col-sm-11.col-xs-10.searchBtnBox > button").click()

more_details = googDrive.find_element(By.CSS_SELECTOR, "#UpdateCarrousel > div > div.ng-scope.list > ul > li.all-messages.ng-scope > a")
more_details.click()
googDrive.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.SPACE)

googDrive.get("https://www.google.com/")
googDrive.find_element(By.NAME, "q").send_keys("ldjkdsf")



# googDrive.back()
# sleep(0.5)
# googDrive.get("https://tourgolan.org.il/golan-trail/")
# food = googDrive.find_element(By.CSS_SELECTOR, "body > div.elementor.elementor-185.elementor-location-header > div > div > section.elementor-element.elementor-element-c5d68b5.elementor-section-stretched.elementor-hidden-tablet.elementor-hidden-phone.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default.elementor-section.elementor-top-section > div > div > div.elementor-element.elementor-element-2306655.elementor-column.elementor-col-20.elementor-top-column > div > div > div > div > ul > li > a > span.elementor-icon-list-text")
# food.click()
# sleep(1)
# action = ActionChains(googDrive)
