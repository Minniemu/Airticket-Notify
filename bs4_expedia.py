url_list = [
    'https://www.expedia.com.tw/Flights-Search?leg1=from%3A%E5%8F%B0%E5%8C%97%20%28TPE-%E6%A1%83%E5%9C%92%E5%9C%8B%E9%9A%9B%E6%A9%9F%E5%A0%B4%29%2Cto%3A%E8%88%8A%E9%87%91%E5%B1%B1%2C%20%E5%8A%A0%E5%88%A9%E7%A6%8F%E5%B0%BC%E4%BA%9E%20%28SFO-%E8%88%8A%E9%87%91%E5%B1%B1%E5%9C%8B%E9%9A%9B%E6%A9%9F%E5%A0%B4%29%2Cdeparture%3A2022%2F3%2F13TANYT&mode=search&options=carrier%3A%2A%2Ccabinclass%3A%2Cmaxhops%3A1%2Cnopenalty%3AN&pageId=0&passengers=adults%3A1%2Cchildren%3A0%2Cinfantinlap%3AN&trip=oneway',
    'https://www.expedia.com.tw/Flights-Search?leg1=from%3A%E5%8F%B0%E5%8C%97%20%28TPE-%E6%A1%83%E5%9C%92%E5%9C%8B%E9%9A%9B%E6%A9%9F%E5%A0%B4%29%2Cto%3A%E8%88%8A%E9%87%91%E5%B1%B1%2C%20%E5%8A%A0%E5%88%A9%E7%A6%8F%E5%B0%BC%E4%BA%9E%20%28SFO-%E8%88%8A%E9%87%91%E5%B1%B1%E5%9C%8B%E9%9A%9B%E6%A9%9F%E5%A0%B4%29%2Cdeparture%3A2022%2F3%2F14TANYT&mode=search&options=carrier%3A%2A%2Ccabinclass%3A%2Cmaxhops%3A1%2Cnopenalty%3AN&pageId=0&passengers=adults%3A1%2Cchildren%3A0%2Cinfantinlap%3AN&trip=oneway',
    'https://www.expedia.com.tw/Flights-Search?leg1=from%3A%E5%8F%B0%E5%8C%97%20%28TPE-%E6%A1%83%E5%9C%92%E5%9C%8B%E9%9A%9B%E6%A9%9F%E5%A0%B4%29%2Cto%3A%E8%88%8A%E9%87%91%E5%B1%B1%2C%20%E5%8A%A0%E5%88%A9%E7%A6%8F%E5%B0%BC%E4%BA%9E%20%28SFO-%E8%88%8A%E9%87%91%E5%B1%B1%E5%9C%8B%E9%9A%9B%E6%A9%9F%E5%A0%B4%29%2Cdeparture%3A2022%2F3%2F17TANYT&mode=search&options=carrier%3A%2A%2Ccabinclass%3A%2Cmaxhops%3A1%2Cnopenalty%3AN&pageId=0&passengers=adults%3A1%2Cchildren%3A0%2Cinfantinlap%3AN&trip=oneway',
    'https://www.expedia.com.tw/Flights-Search?leg1=from%3A%E5%8F%B0%E5%8C%97%20%28TPE-%E6%A1%83%E5%9C%92%E5%9C%8B%E9%9A%9B%E6%A9%9F%E5%A0%B4%29%2Cto%3A%E8%88%8A%E9%87%91%E5%B1%B1%2C%20%E5%8A%A0%E5%88%A9%E7%A6%8F%E5%B0%BC%E4%BA%9E%20%28SFO-%E8%88%8A%E9%87%91%E5%B1%B1%E5%9C%8B%E9%9A%9B%E6%A9%9F%E5%A0%B4%29%2Cdeparture%3A2022%2F3%2F20TANYT&mode=search&options=carrier%3A%2A%2Ccabinclass%3A%2Cmaxhops%3A1%2Cnopenalty%3AN&pageId=0&passengers=adults%3A1%2Cchildren%3A0%2Cinfantinlap%3AN&trip=oneway'
]
import requests
from bs4 import BeautifulSoup

response = requests.get(url_list[0])
soup = BeautifulSoup(response.text, "lxml")
# print(soup.prettify())  #輸出排版後的HTML內容
# result = soup.select_one('')
result = soup.find_all('div',id = 'app-layer-base')
print(len(result))
for entry in result:
    title = entry.find('div', class_='utik-view')
    print(title)
    print()
# result = soup.find("span", class_= 'is-visually-hidden').get_text()
print(result)