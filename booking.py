from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os 
option = Options()
option.add_argument("--disable-notifications")  #不啟用通知
# option.add_argument('headless')
# 開啟瀏覽器視窗(Chrome)
chrome = webdriver.Chrome('./chromedriver', options=option)
chrome.get('https://www.expedia.com.tw/Destinations-In-Taiwan.d176.Flight-Destinations?pwaLob=wizard-flight-pwa')
#單程
chrome.find_element_by_xpath('//*[@id="uitk-tabs-button-container"]/div[1]/li[2]/a/span').click()
#出發地
chrome.find_element_by_xpath('//*[@id="location-field-leg1-origin-menu"]/div[1]/button').click()
departure = chrome.find_element_by_xpath('//*[@id="location-field-leg1-origin"]').send_keys('台北 (TPE - 桃園國際機場)\n')
#目的地
chrome.find_element_by_xpath('//*[@id="location-field-leg1-destination-menu"]/div[1]/button').click()
destination = chrome.find_element_by_xpath('//*[@id="location-field-leg1-destination"]').send_keys('克拉考 (KRK - John Paul II-Balice)\n')
#設定出發日期
departure_time = chrome.find_element_by_xpath('//*[@id="d1-btn"]')
departure_time.click()
#按日期
for i in range(0,6):
    chrome.find_element_by_xpath('//*[@id="wizard-flight-tab-oneway"]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/button[2]').click()
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
chrome.find_element_by_xpath(calander_element[2]).click()
chrome.find_element_by_xpath('//*[@id="wizard-flight-tab-oneway"]/div/div[2]/div/div/div/div/div[2]/div/div[3]/button').click()
#搜尋
chrome.find_element_by_xpath('//*[@id="wizard-flight-pwa-1"]/div[4]/div/button').click()

#取前三
temp_list  = chrome.find_elements_by_class_name('uitk-card-link')
print(temp_list[0].text)
for i in range(3):
    print(temp_list[i].text)

