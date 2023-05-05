import requests
from wxpusher import WxPusher #https://github.com/wxpusher/wxpusher-sdk-python
from bs4 import BeautifulSoup

url0 = 'http://qsxy.zju.edu.cn/'
url1 = 'https://yunfeng.zju.edu.cn/on/main.htm'
url2 = 'https://dqxy.zju.edu.cn/'
url3 = 'http://lantian.zju.edu.cn/ltoffice/'

response0 = requests.get(url0)
response1 = requests.get(url1)
response2 = requests.get(url2)
response3 = requests.get(url3)

response0.encoding = response0.apparent_encoding
response1.encoding = response1.apparent_encoding
response2.encoding = response2.apparent_encoding
response3.encoding = response3.apparent_encoding

soup0 = BeautifulSoup(response0.text,'html.parser')
soup1 = BeautifulSoup(response1.text,'html.parser')
soup2 = BeautifulSoup(response2.text,'html.parser')
soup3 = BeautifulSoup(response3.text,'html.parser')

all_data0 = soup0.select('#wp_news_w13 > ul > li')
all_data1 = soup1.select('#wp_news_w21 > ul > li')
all_data2 = soup2.select('#wp_news_w32 > ul > li')
all_data3 = soup3.select('#wp_news_w53 > ul > li')

message0 = []
message1 = []
message2 = []
message3 = []
#浙江大学求是学院
for i in range(5):
    date = all_data0[i].select('span')[1].text
    title = all_data0[i].select('a')[0]['title']
    href = 'http://qsxy.zju.edu.cn' + all_data0[i].select('a')[0]['href']
    """ print(date)
    print(title)
    print(href) """
    message0.append(date+' '+title+' '+href+'\n')
msg0 = "".join (message0)

#紫云碧峰
for i in range(4):
    """ date = "".join (all_data1[i].find_all('div',class_='news_year')) + "".join (all_data1[i].find_all('div',class_='news_days')) """
    title = all_data1[i].select('a')[0]['title']
    href = 'https://yunfeng.zju.edu.cn/on/main.htm' + all_data1[i].select('a')[0]['href']
    message1.append(title+' '+href+'\n')
msg1 = "".join (message1)

#丹阳青溪
for i in range(4):
    title = all_data2[i].select('a')[0]['title']
    href = 'https://dqxy.zju.edu.cn/' + all_data2[i].select('a')[0]['href']
    message2.append(title+' '+href+'\n')
msg2 = "".join (message2)

#蓝田
for i in range(4):
    title = all_data3[i].select('a')[0]['title']
    href = 'http://lantian.zju.edu.cn/ltoffice/' + all_data3[i].select('a')[0]['href']
    message3.append(title+' '+href+'\n')
msg3 = "".join (message3)

app_token = 'AT_4HZgSky0QUiWEpHsgMvt5f4TfTzfVCVK'   # 本处改成自己的应用 APP_TOKEN
uid_myself = 'UID_Bq6u3Hh9LbrsGvoEV2UJpnMq3bT6'  # 本处改成自己的 UID  若要给自己发在data里加上 "uids":[ uid_myself, ],

def wxpusher_send_by_webapi(msg):
    """利用 wxpusher 的 web api 发送 json 数据包，实现微信信息的发送"""
    webapi = 'http://wxpusher.zjiecode.com/api/send/message'
    data = {
        "appToken":app_token,
        "content":msg,
        "summary":msg[:99], # 该参数可选，默认为 msg 的前10个字符
        "contentType":1,
        "topicIds":[ 9931, ],
        }
    result = requests.post(url=webapi,json=data)
    return result.text

def main(msg):
    result = wxpusher_send_by_webapi(msg)
    print(result)

if __name__ == '__main__':  #作为脚本执行
    main('求是学院\n\n' + msg0 + '\n紫云碧峰\n\n' + msg1 + '\n丹阳青溪\n\n' + msg2 + '\n蓝田\n\n' + msg3)
