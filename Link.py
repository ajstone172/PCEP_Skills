#This is me experimenting with using Python to open a website URL.
#First, I installed selenium and updated my pip.
#Now, I have written a code to open the URL to one of the recipes I referenced in my last project.
#It opens in Firefox, which is my preferred browser.

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://www.newmominanewera.com/2016/12/EasyArrozConLeche.html?m=1")
