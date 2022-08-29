import time
from selenium import webdriver
path="/home/luca/Documents/Code/Selenium/chromedriver"
driver = webdriver.Chrome("/home/luca/Documents/Code/Selenium/chromedriver")
driver.get("file:///home/luca/Documents/Recherche%20%C2%B7%20Info%20sant%C3%A9.html")
liste=driver.find_elements_by_id('morphsearch')
print(liste)