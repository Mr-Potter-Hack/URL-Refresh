from time import sleep
from selenium import webdriver
from urllib.request import Request, urlopen
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b


time_to_sleep = int(input("Enter The Time to Refresh After :- "))
link = input("Full URL :- ")

driver = webdriver.Chrome('C://Users/PC/Desktop/YT Bot/chromedriver.exe')

def launch_browser():
    global driver
    driver.get(link)
    while True:
        driver.refresh()
        print("refreshing")
        sleep(time_to_sleep)
    return driver

driver = launch_browser()
