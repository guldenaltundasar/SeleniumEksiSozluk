from selenium import webdriver
import time

driver_path="/Users/galtu/Downloads/selenium/chromedriver"
browser=webdriver.Chrome(driver_path)
url = "https://eksisozluk.com/eksi-sozluk--31966"
browser.get(url)
time.sleep(5)
elements = browser.find_elements_by_css_selector(".content")
for element in elements:
    print("***********************")
    print(element.text)
browser.close()
