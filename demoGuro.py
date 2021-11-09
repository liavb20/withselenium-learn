from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# driver.implicitly.wait(10) --->
# הסלניום רץ מהר ואם התוכנית לא מוצאת את אחד האלאמנטים הפקודה גורמת לתכנית לחכות מספר שניות לפני שהיא קורסת כדי שאולי יופיע האלמנט

# get_attribute("value") בודק אם בשורת חיפוש (כמו גוגל) מופיע טקסט ואפשר להדפיס אותו ולבצע עליו פעולות



ser = Service(r"C:\selen\chromedriver.exe")
drive = webdriver.Chrome(service=ser)
drive.get("http://demo.guru99.com/test/newtours/")
drive.maximize_window()
drive.find_element(By.NAME, "userName").send_keys("tutorial")
drive.find_element(By.NAME, "password").send_keys("tutorial")
drive.find_element(By.NAME, "submit").click()
drive.find_element(By.LINK_TEXT, "Flights").click()
drive.find_element(By.CSS_SELECTOR, "[value='oneway']").click()
drive.find_element(By.CSS_SELECTOR, "[value='First']").click()
departure = drive.find_element(By.NAME, "passCount")
departure_dropdown = Select(departure)
departure_dropdown.select_by_visible_text('2')
departure_dropdown2 = Select(drive.find_element(By.NAME, "fromPort"))
departure_dropdown2.select_by_visible_text('New York')
Select(drive.find_element(By.NAME, "fromDay")).select_by_visible_text('18')
Select(drive.find_element(By.NAME, "toPort")).select_by_visible_text('Portland')
Select(drive.find_element(By.NAME, "toDay")).select_by_value('30')
drive.find_element(By.NAME, "findFlights").click()
time.sleep(2)
drive.find_element(By.CSS_SELECTOR, "img[src='images/home.gif']").click()
time.sleep(5)
drive.close()