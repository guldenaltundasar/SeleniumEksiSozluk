from selenium import webdriver
import random
import time

driver_path = "/Users/galtu/Downloads/selenium/chromedriver"
browser = webdriver.Chrome(driver_path)
url = "https://eksisozluk.com/eksi-sozluk--31966?p="

pageCount = 1
entries = []
entryCount = 1

while pageCount <= 10:
     randomPage = random.randint(1,2527)
     newUrl = url + str(randomPage)
     browser.get(newUrl)

     elements = browser.find_elements_by_css_selector(".content")
     for element in elements:
       entries.append(element.text)
     time.sleep(3)
     pageCount += 1

for entry in entries:
        print(str(entryCount) + "******************************")
        print(entry)
        entryCount += 1


browser.close()
