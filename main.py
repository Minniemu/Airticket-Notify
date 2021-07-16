from logging import error
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
import time
import os 
calander_element = [
    '//*[@id="wizard-flight-tab-oneway"]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[1]/button',
    '//*[@id="wizard-flight-tab-oneway"]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[2]/button',
    '//*[@id="wizard-flight-tab-oneway"]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[3]/button',
    '//*[@id="wizard-flight-tab-oneway"]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[4]/button',
    '//*[@id="wizard-flight-tab-oneway"]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[5]/button',
    '//*[@id="wizard-flight-tab-oneway"]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[6]/button',
    '//*[@id="wizard-flight-tab-oneway"]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[7]/button',
    '//*[@id="wizard-flight-tab-oneway"]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[5]/td[1]/button',
    '//*[@id="wizard-flight-tab-oneway"]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[5]/td[2]/button'
    ]
departure_date = ['2/20','2/21','2/22','2/23','2/24','2/25','2/26','2/27','2/28']
index = 0
def one_way():
    #單程
    chrome.find_element_by_xpath('//*[@id="uitk-tabs-button-container"]/div[1]/li[2]/a/span').click()
    dep_des()

def dep_des():
    #出發地
    chrome.find_element_by_xpath('//*[@id="location-field-leg1-origin-menu"]/div[1]/button').click()
    departure = chrome.find_element_by_xpath('//*[@id="location-field-leg1-origin"]').send_keys('台北 (TPE - 桃園國際機場)\n')
    #目的地
    chrome.find_element_by_xpath('//*[@id="location-field-leg1-destination-menu"]/div[1]/button').click()
    destination = chrome.find_element_by_xpath('//*[@id="location-field-leg1-destination"]').send_keys('克拉考 (KRK - John Paul II-Balice)\n')
    #設定出發日期
    departure_time = chrome.find_element_by_xpath('//*[@id="d1-btn"]')
    departure_time.click()
    date()

def date():
    #按日期
    for i in range(0,6):
        chrome.find_element_by_xpath('//*[@id="wizard-flight-tab-oneway"]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/button[2]').click()
        time.sleep(1)
    
    chrome.find_element_by_xpath(calander_element[index]).click()
    chrome.find_element_by_xpath('//*[@id="wizard-flight-tab-oneway"]/div/div[2]/div/div/div/div/div[2]/div/div[3]/button').click()
    #搜尋
    chrome.find_element_by_xpath('//*[@id="wizard-flight-pwa-1"]/div[4]/div/button').click()
    get_data()

def get_data():
    #取前三
    print("Date = ",departure_date[index])
    error_time = 0
    try:
        temp_list  = chrome.find_elements_by_class_name('uitk-card-link')
        if temp_list:
            for i in range(3):
                print(temp_list[i].text)
        elif error_time >= 3:
            # temp_list = chrome.find_elements_by_xpath('//*[@id="AQqiAgqMAnY1LXNvcy1kOWRmZTcwNzk5YjU0NmY1YmZjNWZlYzc1YTU5NjQ3ZC0yNy0xfjIuU35BUW9DQ0Q0U0J3alRiUkFKR0U4Z0J5QUJJQXdnRFNBSktBSllBWEFBfkFRcG1DaDhJdzdBQkVnTTBOamtZOHlNZ3h6SW8yTDJGQWpEUXZvVUNPRXhBQUZnQkNpQUl5NWdCRWdNNE9EZ1l4eklnZ0pNQktLLV9oUUl3bU1XRkFqaEZRQUZZQVFvaENNdVlBUklFTVRrNU9SaUFrd0VncWxRb19NV0ZBakRxeG9VQ09FeEFBVmdCRWdvSUFSQUJHQUVxQWt0TUdBRWlCQWdCRUFFb0FpZ0RLQVF3QVERAAAAAEC-2EAiAQEqBRIDCgExEicKFgoKMjAyMi0wMi0yMxIDVFBFGgNLUksSBxIFQ09BQ0gaAhABIAEgAQ=="]/div/div/div/button')
            print("temp_list is empty")
            chrome.back()
        else:
            chrome.refresh()
        chrome.back()
    except Exception as e: 
        error_time += 1
        print(e)
        time.sleep(3)

option = Options()
option.add_argument("--disable-notifications")  #不啟用通知
# option.add_argument('headless')
# 開啟瀏覽器視窗(Chrome)
chrome = webdriver.Chrome('./chromedriver', options=option)
chrome.get('https://www.expedia.com.tw/Destinations-In-Taiwan.d176.Flight-Destinations?pwaLob=wizard-flight-pwa')
for i in range(len(calander_element)):
    # ua = UserAgent()
    # a = ua.random
    # user_agent = ua.random
    # print(user_agent)
    # option.add_argument(f'user-agent={user_agent}')
    # chrome = webdriver.Chrome('./chromedriver', options=option)
    try:
        one_way()
        index += 1
        # chrome.quit()
    except Exception as e: 
        print(e)
        time.sleep(3)
chrome.quit()


