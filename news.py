import datetime
import requests
from bs4 import BeautifulSoup

url = 'http://qsxy.zju.edu.cn/'
response = requests.get(url)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text,'html.parser')
all_data = soup.select('#wp_news_w13 > ul > li')
for i in range(5):
    date = all_data[i].select('span')[1].text
    title = all_data[i].select('a')[0].text
    href = 'http://qsxy.zju.edu.cn' + all_data[0].select('a')[0]['href']
    print(date)
    print(title)
    print(href)