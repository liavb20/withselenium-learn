from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.select import Select


service = Service(r"C:\selen\geckodriver.exe")
firefoxDrive = webdriver.Firefox(service=service)
firefoxDrive.get("https://phptravels.net/api/admin")
firefoxDrive.maximize_window()
firefoxDrive.implicitly_wait(10)
firefoxDrive.find_element(By.CSS_SELECTOR, "input[type = 'text']").send_keys("admin@phptravels.com")
firefoxDrive.find_element(By.NAME, "password").send_keys("demoadmin")
firefoxDrive.find_element(By.CSS_SELECTOR, "ins[class = 'iCheck-helper']").click()
firefoxDrive.find_element(By.CSS_SELECTOR, "button[data-wow-delay='s']").click()
checkString = firefoxDrive.find_element(By.CSS_SELECTOR, "a[class='navbar-brand']>strong>small").text
if checkString == "DASHBOARD":
    print('success')
else:
    print('fail')
firefoxDrive.find_element(By.LINK_TEXT, "Cars").click()
sleep(1)
firefoxDrive.find_element(By.LINK_TEXT, "Locations").click()


# sleep(1.2)
# # firefoxDrive.find_element(By.CSS_SELECTOR, "li[id='logout']>a>strong").click()
# firefoxDrive.find_element(By.ID, "logout").click()


