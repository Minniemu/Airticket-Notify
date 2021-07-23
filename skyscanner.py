import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
import time
from fake_useragent import UserAgent

ua = UserAgent()
options = Options()
user_agent = ua.chrome #代理伺服器
options.add_argument("--disable-notifications")  #不啟用通知
options.add_argument("user-agent={}".format(user_agent))   #代理伺服器
chrome = webdriver.Chrome(executable_path="D:\Github Repo\Air Ticket\chromedriver.exe",chrome_options=options)
chrome.get("https://www.skyscanner.com.tw/transport/flights/tpe/krk/220221/220228/?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27543787&inboundaltsenabled=false&infants=0&originentityid=27547236&outboundaltsenabled=false&preferdirects=false&preferflexible=false&ref=home&rtn=1")
result = chrome.find_element_by_id('app-root')
length = 0

while True:
    try:
        x = chrome.find_element_by_xpath('//*[@id="app-root"]/div[1]/div/div[2]/div[2]/div[1]/div[2]/button[1]/div/div/span')
        print(x.text)
        #出發時間
        departure_time = chrome.find_element_by_xpath('//*[@id="app-root"]/div[1]/div/div[2]/div[2]/div[1]/div[3]/div[1]/div/div/a/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/div[1]/span[1]/div/span')
        print("出發時間 = ",departure_time.text)
        #到達時間
        arrive_time = chrome.find_element_by_xpath('//*[@id="app-root"]/div[1]/div/div[2]/div[2]/div[1]/div[3]/div[1]/div/div/a/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/div[3]/span[1]/div/span')
        print("抵達時間 = ",arrive_time.text)
        #價錢
        price = chrome.find_element_by_xpath('//*[@id="app-root"]/div[1]/div/div[2]/div[2]/div[1]/div[3]/div[1]/div/div/a/div/div[3]/div/div/div/span')
        print("價錢 = ",price.text)
        #轉機次數
        turnaround = chrome.find_element_by_xpath('//*[@id="app-root"]/div[1]/div/div[2]/div[2]/div[1]/div[3]/div[1]/div/div/a/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/span')
        print(turnaround.text)
        #飛行時數
        duration = chrome.find_element_by_xpath('//*[@id="app-root"]/div[1]/div/div[2]/div[2]/div[1]/div[3]/div[1]/div/div/a/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/div[2]/span')
        print(duration.text)
        #航空公司
        airline = chrome.find_element_by_xpath('//*[@id="app-root"]/div[1]/div/div[2]/div[2]/div[1]/div[3]/div[1]/div/div/a/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/span')
        print(airline.text)

        break
    except :
        time.sleep(1)
print(length)