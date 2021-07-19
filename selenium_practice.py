from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os 
options = Options()
options.add_argument("--disable-notifications")  #不啟用通知
# 開啟瀏覽器視窗(Chrome)
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get("https://www.skyscanner.com.tw/")
#出發地&目的地
departure = chrome.find_element_by_css_selector("#fsc-origin-search")
departure.send_keys("台北桃園 (TPE)")
destination = chrome.find_element_by_css_selector("#fsc-destination-search")
destination.send_keys("克拉考 (KRK)")
#設定出發日期
departure_time = chrome.find_element_by_id("depart-fsc-datepicker-button")
departure_time.click()
s = chrome.find_element_by_xpath("//*[@id='depart-calendar__bpk_calendar_nav_select']").click()
select = Select(chrome.find_element_by_xpath("//*[@id='depart-calendar__bpk_calendar_nav_select']"))
select.select_by_value("2022-02")
chrome.find_element_by_xpath("//*[@id='depart-fsc-datepicker-popover']/div/div/div[2]/div/table/tbody/tr[4]/td[2]/button").click()
#設定離開日期
return_time = chrome.find_element_by_id("return-fsc-datepicker-button").click()
chrome.find_element_by_xpath("//*[@id='return-calendar__bpk_calendar_nav_select']").click()
select = Select(chrome.find_element_by_xpath("//*[@id='return-calendar__bpk_calendar_nav_select']"))
select.select_by_value("2022-02")
chrome.find_element_by_xpath("//*[@id='return-fsc-datepicker-popover']/div/div/div[2]/div/table/tbody/tr[5]/td[2]/button/span").click()
#搜尋
chrome.find_element_by_xpath("//*[@id='flights-search-controls-root']/div/div/form/div[3]/button").click()

